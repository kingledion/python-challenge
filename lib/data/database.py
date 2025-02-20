import logging
from contextlib import contextmanager
from typing import Generator, Self

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from lib.model import Base


class DB:
    def __init__(self, engine: Engine):

        self._engine: Engine = engine

    @classmethod
    def new(self, echo: bool = False) -> Self:
        engine = create_engine(
            "sqlite://",
            connect_args={"check_same_thread": False},
            poolclass=StaticPool,
            echo=echo,
        )
        return self(engine)

    @contextmanager
    def get_session(self) -> Generator[Session, None, None]:
        """
        Returns a new database session for each call. This ensures that each
        operation gets its own transaction context.
        """
        with Session(self._engine) as session:
            yield session
            # the context automatically closes this session

    def init_db(self) -> None:
        logging.info("migrating data tables...")
        Base.metadata.create_all(self._engine)
        logging.info("SQLAlchemy migration complete...")

    def close(self) -> None:
        self._engine.dispose()
