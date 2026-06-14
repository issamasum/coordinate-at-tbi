# __author__ = Issa Masumbuko

"""Database-backed EventParticipant and EventParticipantRole models."""

import enum
from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import Column, ForeignKey, Integer, UniqueConstraint
from sqlmodel import Field, Relationship, SQLModel, Enum

if TYPE_CHECKING:
    from .person import Person
    from .event import Event
    from .dorm import DormAssignment
    from .orientation import OrientationParticipant


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
    DORM_COLLABORATOR = "dorm collaborator"
    DORM_COORDINATOR = "dorm coordinator"
    TUTOR = "tutor"


class EventParticipant(SQLModel, table=True):
    """Represents a person's registration in a specific event."""

    __tablename__ = "eventparticipant"
    __table_args__ = (
        UniqueConstraint("person_id", "event_id", name="unique_participation"),
    )

    id: int = Field(sa_column=Column(Integer, primary_key=True, autoincrement=True))
    person_id: int = Field(
        sa_column=Column(Integer, ForeignKey("person.id"), nullable=False)
    )
    event_id: int = Field(
        sa_column=Column(Integer, ForeignKey("event.id"), nullable=False)
    )
    overnight_status: Optional[OvernightStatus] = Field(
        default=None,
        sa_column=Column(
            Enum(OvernightStatus, values_callable=lambda e: [m.value for m in e]),
            nullable=True,
        ),
    )
    attendance_status: Optional[AttendanceStatus] = Field(
        default=None,
        sa_column=Column(
            Enum(AttendanceStatus, values_callable=lambda e: [m.value for m in e]),
            nullable=True,
        ),
    )
    person: Optional["Person"] = Relationship(back_populates="event_participations")
    event: Optional["Event"] = Relationship(back_populates="participants")
    roles: List["EventParticipantRole"] = Relationship(back_populates="participant")
    dorm_assignment: Optional["DormAssignment"] = Relationship(
        back_populates="participant"
    )

    orientation_membership: Optional["OrientationParticipant"] = Relationship(
        back_populates="participant"
    )


class EventParticipantRole(SQLModel, table=True):
    """Represents a role held by a participant at a specific event."""

    __tablename__ = "eventparticipantrole"
    __table_args__ = (
        UniqueConstraint("participant_id", "role", name="unique_participant_role"),
    )

    id: int = Field(sa_column=Column(Integer, primary_key=True, autoincrement=True))
    participant_id: int = Field(
        sa_column=Column(Integer, ForeignKey("eventparticipant.id"), nullable=False)
    )
    role: ParticipantRole = Field(
        sa_column=Column(
            Enum(ParticipantRole, values_callable=lambda e: [m.value for m in e]),
            nullable=False,
        )
    )
    participant: Optional["EventParticipant"] = Relationship(back_populates="roles")