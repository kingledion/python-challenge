from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from lib.model import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int | None] = mapped_column(
        primary_key=True,
        nullable=False,
    )

    date_joined: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )
    last_login: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    o2x_id: Mapped[str]
    email: Mapped[str]
    phone: Mapped[str]
    first_name: Mapped[str]
    last_name: Mapped[str]

    gender: Mapped[str | None]
    height: Mapped[Decimal | None] = mapped_column(
        Numeric(precision=6, scale=2),
        nullable=True,
    )
    weight: Mapped[Decimal | None] = mapped_column(
        Numeric(precision=6, scale=2),
        nullable=True,
    )

    is_active: Mapped[bool]
    is_onboarded: Mapped[bool]
    is_superuser: Mapped[bool]
    is_staff: Mapped[bool]
