# __author__ = Issa Masumbuko

"""Database-backed cottage models"""

import enum
from typing import TYPE_CHECKING, List

from sqlalchemy import Boolean, Column, Integer, Text, UniqueConstraint
from sqlmodel import Field, Relationship, SQLModel, Enum

if TYPE_CHECKING:
    from .dorm import Dorm


class CottageGender(str, enum.Enum):
    MALE = "Male"
    FEMALE = "Female"


class Cottage(SQLModel, table=True):
    """Represents a cottage used for overnight events at the Triangle Baha'i Institute."""

    __tablename__ = "cottage"
    __table_args__ = (
        UniqueConstraint("name", name="unique_cottage_name"),
    )

    id: int = Field(sa_column=Column(Integer, primary_key=True, autoincrement=True))
    name: str = Field(sa_column=Column(Text, nullable=False))
    gender: CottageGender = Field(
        sa_column=Column(
            Enum(CottageGender, values_callable=lambda e: [m.value for m in e]),
            nullable=False,
        )
    )
    is_active: bool = Field(sa_column=Column(Boolean, nullable=False, default=True))
    rooms: List["Dorm"] = Relationship(back_populates="cottage")