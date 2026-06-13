# __author__ = Issa Masumbuko

"""Database-backed user / authentication models"""

import enum
from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, Text
from sqlmodel import Field, Relationship, SQLModel, func, Enum, UniqueConstraint

if TYPE_CHECKING:
    from .person import Person


class UserRole(str, enum.Enum):
    MAIN_COORDINATOR = "main_coordinator"
    COORDINATOR = "coordinator"


class User(SQLModel, table=True):
    """Represents a login-enabled coordinator account linked to a Person record."""

    __tablename__ = "user"
    __table_args__ = (
        UniqueConstraint("email", name="unique_user_email"),
        UniqueConstraint("person_id", name="unique_user_person"),
    )

    id: int = Field(sa_column=Column(Integer, primary_key=True, autoincrement=True))
    person_id: int = Field(
        sa_column=Column(Integer, ForeignKey("person.id"), nullable=False)
    )
    email: str = Field(sa_column=Column(Text, nullable=False))
    hashed_password: str = Field(sa_column=Column(Text, nullable=False))
    role: UserRole = Field(
        sa_column=Column(
            Enum(UserRole, values_callable=lambda e: [m.value for m in e]),
            nullable=False,
        )
    )
    is_active: bool = Field(sa_column=Column(Boolean, nullable=False, default=True))
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False),
        default=None,
    )
    last_login_at: Optional[datetime] = Field(
        default=None, sa_column=Column(DateTime(timezone=True), nullable=True)
    )
    person: Optional["Person"] = Relationship(back_populates="user")