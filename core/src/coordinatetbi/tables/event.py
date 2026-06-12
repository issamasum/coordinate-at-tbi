# __author__ = Issa Masumbuko

"""Database-backed event models"""
import enum
from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, Text, ForeignKey, UniqueConstraint
from sqlmodel import (
    Field, 
    SQLModel,
    func,
    Enum,
)

class EventStatus(str, enum.Enum):
    DRAFT = "draft"
    PUBLISHED = "published"
    CANCELED = "canceled"
 
 
class DormStrategy(str, enum.Enum):
    FAMILIARITY = "familiarity"
    DIVERSIFY = "diversify"
 
 
class OvernightStatus(str, enum.Enum):
    STAYING = "Staying"
    NOT_STAYING = "Not Staying"
 
 
class AttendanceStatus(str, enum.Enum):
    REGISTERED = "registered"
    ATTENDED = "attended"
    ABSENT = "absent"
 
 
class ParticipantRole(str, enum.Enum):
    PARTICIPANT = "participant"
    ORIENTATION_FACILITATOR = "orientation facilitator"
    TUTOR = "tutor"

class Event(SQLModel, table=True):
    """Represents an event organized by the Triangle Baha'i Institute."""

    id: int = Field(
        sa_column=Column(Integer, primary_key=True, autoincrement=True)
    )
    name: str = Field(
            sa_column=Column(Text, nullable=False)
    )
    location: str = Field(
            sa_column=Column(Text, nullable=False)
    )
    start_date: datetime = Field(
        sa_column=Column(
            DateTime(timezone=False),
            nullable=False
        )
    )
    end_date: datetime = Field(
        sa_column=Column(
            DateTime(timezone=False),
            nullable=False
        )
    )
    overnight: bool = Field()
    dorm_strategy: DormStrategy = Field(
        sa_column=Column(
            Enum(DormStrategy, values_callable=lambda e: [m.value for m in e]),
            nullable=True
        )
    )
    status: EventStatus = Field(
        sa_column=Column(
            Enum(EventStatus, values_callable=lambda e: [m.value for m in e]),
            nullable=False
        )
    )
    updated_by: int = Field(
        sa_column=Column(Integer, ForeignKey("person.id"), nullable=True)
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
    deleted_at: datetime = Field(
        sa_column=Column(
            DateTime(timezone=True),
            server_default=func.now(),
            onupdate=func.now(),
            nullable=False,
        ),
        default=None,
    )

class EventParticipant(SQLModel, table=True):
    """Represents a person participating in an event organized by the Triangle Baha'i Institute."""

    __tablename__ = "event_participant"
    __table_args__ = (
        UniqueConstraint("person_id", "event_id", name="unique_participation"),
    )
    id: int = Field(
        sa_column=Column(Integer, primary_key=True, autoincrement=True)
    )
    person_id: int = Field(
        sa_column=Column(Integer, ForeignKey("person.id"), nullable=False)
    )
    event_id: int = Field(
        sa_column=Column(Integer, ForeignKey("event.id"), nullable=False)
    )
    overnight_status: OvernightStatus = Field(
        sa_column=Column(
            Enum(OvernightStatus, values_callable=lambda e: [m.value for m in e]),
            nullable=True
        )
    )
    attendence_status: AttendanceStatus = Field(
        sa_column=Column(
            Enum(AttendanceStatus, values_callable=lambda e: [m.value for m in e]),
            nullable=True
        )
    )


class EventParticipantRole(SQLModel, table=True):
    """Represents a role that a person can have at an event organized by the Triangle Baha'i Institute."""
    __tablename__ = "event_participant_role"
    id: int = Field(
        sa_column=Column(Integer, primary_key=True, autoincrement=True)
    )
    participant_id: int = Field(
        sa_column=Column(Integer, ForeignKey("event_participant.id"), nullable=False)
    )
    role: ParticipantRole = Field(
        sa_column=Column(
            Enum(ParticipantRole, values_callable=lambda e: [m.value for m in e]),
            nullable=False
        )
    )