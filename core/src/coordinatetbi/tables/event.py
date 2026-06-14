# __author__ = Issa Masumbuko

"""Database-backed Event model."""

import enum
from datetime import datetime
from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, Text
from sqlmodel import Field, Relationship, SQLModel, func, Enum

if TYPE_CHECKING:
    from .person import Person
    from .event_participant import EventParticipant
    from .event_course import EventCourse
    from .dorm import EventDormRoom
    from .orientation import OrientationGroup
    from .study_circle import StudyCircle, StudyCircleSession


class EventStatus(str, enum.Enum):
    DRAFT = "draft"
    PUBLISHED = "published"
    CANCELED = "canceled"


class DormStrategy(str, enum.Enum):
    FAMILIARITY = "familiarity"
    DIVERSIFY = "diversify"


class Event(SQLModel, table=True):
    """Represents an event organized by the Triangle Baha'i Institute."""

    __tablename__ = "event"

    id: int = Field(sa_column=Column(Integer, primary_key=True, autoincrement=True))
    name: str = Field(sa_column=Column(Text, nullable=False))
    location: str = Field(sa_column=Column(Text, nullable=False))
    start_date: datetime = Field(
        sa_column=Column(DateTime(timezone=False), nullable=False)
    )
    end_date: datetime = Field(
        sa_column=Column(DateTime(timezone=False), nullable=False)
    )
    overnight: bool = Field(sa_column=Column(Boolean, nullable=False, default=False))
    dorm_strategy: Optional[DormStrategy] = Field(
        default=None,
        sa_column=Column(
            Enum(DormStrategy, values_callable=lambda e: [m.value for m in e]),
            nullable=True,
        ),
    )
    status: EventStatus = Field(
        sa_column=Column(
            Enum(EventStatus, values_callable=lambda e: [m.value for m in e]),
            nullable=False,
        )
    )
    updated_by: Optional[int] = Field(
        default=None,
        sa_column=Column(Integer, ForeignKey("person.id"), nullable=True),
    )
    created_at: datetime = Field(
        sa_column=Column(
            DateTime(timezone=True), server_default=func.now(), nullable=False
        ),
        default=None,
    )
    updated_at: datetime = Field(
        sa_column=Column(
            DateTime(timezone=True),
            server_default=func.now(),
            onupdate=func.now(),
            nullable=False,
        ),
        default=None,
    )
    deleted_at: Optional[datetime] = Field(
        default=None, sa_column=Column(DateTime(timezone=True), nullable=True)
    )
    last_updated_by: Optional["Person"] = Relationship(
        sa_relationship_kwargs={"foreign_keys": "[Event.updated_by]"}
    )
    participants: List["EventParticipant"] = Relationship(back_populates="event")

    event_courses: List["EventCourse"] = Relationship(back_populates="event")
    event_dorm_rooms: List["EventDormRoom"] = Relationship(back_populates="event")
    orientation_groups: List["OrientationGroup"] = Relationship(back_populates="event")
    study_circles: List["StudyCircle"] = Relationship(back_populates="event")
    study_circle_sessions: List["StudyCircleSession"] = Relationship(
        back_populates="event"
    )