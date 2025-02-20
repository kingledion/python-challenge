from datetime import datetime
from typing import Any, Generator, Sequence

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from lib.data import DB, Session
from notify.model import Notification, NotificationCategory
from notify.routes import notify
from user.model import User


@pytest.fixture()
def client(database: DB) -> Generator[TestClient, None, None]:

    app = FastAPI()
    app.include_router(notify(database))

    yield TestClient(app)


@pytest.fixture()
def database() -> Generator[DB, None, None]:

    db = DB.new(echo=True)
    db.init_db()

    yield db

    db.close()


@pytest.fixture()
def session(database: DB) -> Generator[Session, None, None]:
    with database.get_session() as s:
        yield s


def populate(session: Session, data: Any) -> Any:
    session.add(data)
    session.commit()
    session.refresh(data)
    return data


class TestData:
    notifications: Sequence[Notification]

    def __init__(
        self,
        users: Sequence[User],
        notifications: Sequence[Notification],
    ):
        self.users = users
        self.notifications = notifications


@pytest.fixture()
def testdata(session: Session) -> TestData:

    user1 = populate(
        session,
        User(
            id=1,
            date_joined=datetime.now(),
            last_login=datetime.now(),

            o2x_id=12345,
            email="user.zero@example.org",
            phone="123-456-7890",
            first_name="user",
            last_name="zero",

            is_active=True,
            is_onboarded=True,
            is_superuser=True,
            is_staff=True,
        ),
    )

    notification1 = populate(
        session,
        Notification(
            id=1,
            user_id=user1.id,
            title="Title of message",
            body="Important message",
            category=NotificationCategory.chat,
            payload={"message_id": 12345},
        ),
    )

    notification2 = populate(
        session,
        Notification(
            id=2,
            user_id=user1.id,
            title="Another message",
            body="More important information",
            category=NotificationCategory.chat,
            payload={"message_id": 12346},
        ),
    )

    notification3 = populate(
        session,
        Notification(
            id=3,
            user_id=user1.id,
            title="Still getting messages",
            body="But this one is alrady acknoweldged",
            category=NotificationCategory.chat,
            payload={"message_id": 12347},
        ),
    )

    return TestData([user1], [notification1, notification2, notification3])
