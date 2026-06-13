# __author__ = Issa Masumbuko

"""Database-backed dorm-facing models"""

import enum
from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import Boolean, Column, ForeignKey, Integer, Text, UniqueConstraint
from sqlmodel import Field, Relationship, SQLModel, Enum

if TYPE_CHECKING:
    from .cottage import Cottage
    from .event import Event
    from .event_participant import EventParticipant


class DormAssignmentStatus(str, enum.Enum):
    DRAFT = "draft"
    CONFIRMED = "confirmed"
    CANCELED = "canceled"


class Dorm(SQLModel, table=True):
    """Represents a dorm room at the Triangle Baha'i Institute facility."""

    __tablename__ = "dorm"
    __table_args__ = (
        UniqueConstraint("name", "cottage_id", name="unique_dorm_name_per_cottage"),
    )

    id: int = Field(sa_column=Column(Integer, primary_key=True, autoincrement=True))
    name: str = Field(sa_column=Column(Text, nullable=False))
    cottage_id: int = Field(
        sa_column=Column(Integer, ForeignKey("cottage.id"), nullable=False)
    )
    capacity: int = Field(sa_column=Column(Integer, nullable=False))
    is_active: bool = Field(sa_column=Column(Boolean, nullable=False, default=True))


    cottage: Optional["Cottage"] = Relationship(back_populates="rooms")

    event_dorm_rooms: List["EventDormRoom"] = Relationship(back_populates="dorm")


class EventDormRoom(SQLModel, table=True):
    """Represents a dorm room activated for a specific overnight event."""

    __tablename__ = "eventdormroom"
    __table_args__ = (
        UniqueConstraint("dorm_id", "event_id", name="unique_event_dorm_room"),
    )

    id: int = Field(sa_column=Column(Integer, primary_key=True, autoincrement=True))
    dorm_id: int = Field(
        sa_column=Column(Integer, ForeignKey("dorm.id"), nullable=False)
    )
    event_id: int = Field(
        sa_column=Column(Integer, ForeignKey("event.id"), nullable=False)
    )

    dorm: Optional["Dorm"] = Relationship(back_populates="event_dorm_rooms")

    event: Optional["Event"] = Relationship(back_populates="event_dorm_rooms")

    assignments: List["DormAssignment"] = Relationship(back_populates="event_dorm_room")


class DormAssignment(SQLModel, table=True):
    """Represents a participant's dorm assignment for an overnight event."""

    __tablename__ = "dormassignment"
    __table_args__ = (
        UniqueConstraint("event_dorm_id", "participant_id", name="unique_dorm_assignment"),
    )

    id: int = Field(sa_column=Column(Integer, primary_key=True, autoincrement=True))
    event_dorm_id: int = Field(
        sa_column=Column(Integer, ForeignKey("eventdormroom.id"), nullable=False)
    )
    participant_id: int = Field(
        sa_column=Column(Integer, ForeignKey("eventparticipant.id"), nullable=False)
    )
    status: DormAssignmentStatus = Field(
        sa_column=Column(
            Enum(DormAssignmentStatus, values_callable=lambda e: [m.value for m in e]),
            nullable=False,
        )
    )

    event_dorm_room: Optional["EventDormRoom"] = Relationship(back_populates="assignments")

    participant: Optional["EventParticipant"] = Relationship(
        back_populates="dorm_assignment"
    )