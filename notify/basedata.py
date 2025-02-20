from datetime import datetime

from lib.data import DB
from user.model import User


def populate(db: DB) -> None:

    user1 = User(
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
    )

    with db.get_session() as session:
        session.add(user1)
        session.commit()
