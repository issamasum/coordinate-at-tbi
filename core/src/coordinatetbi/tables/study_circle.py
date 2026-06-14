# __author__ = Issa Masumbuko

"""Database-backed study circle models"""

import enum
from datetime import datetime
from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, Text, UniqueConstraint
from sqlmodel import Field, Relationship, SQLModel, func, Enum

if TYPE_CHECKING:
    from .person import Person
    from .course import Course
    from .event import Event


class StudyCircleStatus(str, enum.Enum):
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    CANCELED = "Canceled"


class MemberStatus(str, enum.Enum):
    ACTIVE = "active"
    COMPLETED = "completed"
    DROPPED = "dropped"


class SessionStatus(str, enum.Enum):
    DRAFT = "draft"
    CONFIRMED = "confirmed"
    CANCELED = "canceled"


class AttendanceRole(str, enum.Enum):
    TUTOR = "Tutor"
    PARTICIPANT = "Participant"


class StudyCircle(SQLModel, table=True):
    """Represents a study circle, optionally tied to an event."""

    __tablename__ = "studycircle"
    __table_args__ = (
        UniqueConstraint("name", "event_id", name="unique_study_circle_name_event"),
    )

    id: int = Field(sa_column=Column(Integer, primary_key=True, autoincrement=True))
    name: str = Field(sa_column=Column(Text, nullable=False))
    status: StudyCircleStatus = Field(
        sa_column=Column(
            Enum(StudyCircleStatus, values_callable=lambda e: [m.value for m in e]),
            nullable=False,
        )
    )
    course_id: int = Field(
        sa_column=Column(Integer, ForeignKey("course.id"), nullable=False)
    )
    event_id: Optional[int] = Field(
        default=None,
        sa_column=Column(Integer, ForeignKey("event.id"), nullable=True),
    )
    course: Optional["Course"] = Relationship(back_populates="study_circles")
    event: Optional["Event"] = Relationship(back_populates="study_circles")
    members: List["StudyCircleMember"] = Relationship(back_populates="study_circle")
    sessions: List["StudyCircleSession"] = Relationship(back_populates="study_circle")


class StudyCircleMember(SQLModel, table=True):
    """Represents a person's membership in a study circle."""

    __tablename__ = "studycirclemember"
    __table_args__ = (
        UniqueConstraint("study_circle_id", "person_id", name="unique_study_circle_member"),
    )

    id: int = Field(sa_column=Column(Integer, primary_key=True, autoincrement=True))
    study_circle_id: int = Field(
        sa_column=Column(Integer, ForeignKey("studycircle.id"), nullable=False)
    )
    person_id: int = Field(
        sa_column=Column(Integer, ForeignKey("person.id"), nullable=False)
    )
    status: MemberStatus = Field(
        sa_column=Column(
            Enum(MemberStatus, values_callable=lambda e: [m.value for m in e]),
            nullable=False,
        )
    )
    study_circle: Optional["StudyCircle"] = Relationship(back_populates="members")

    person: Optional["Person"] = Relationship(back_populates="study_circle_memberships")
    attendance_records: List["StudyCircleAttendance"] = Relationship(back_populates="member")


class StudyCircleSession(SQLModel, table=True):
    """Represents a single session (meeting) of a study circle."""

    __tablename__ = "studycirclesession"

    id: int = Field(sa_column=Column(Integer, primary_key=True, autoincrement=True))
    study_circle_id: int = Field(
        sa_column=Column(Integer, ForeignKey("studycircle.id"), nullable=False)
    )
    event_id: Optional[int] = Field(
        default=None,
        sa_column=Column(Integer, ForeignKey("event.id"), nullable=True),
    )
    session_number: int = Field(sa_column=Column(Integer, nullable=False))
    session_date: datetime = Field(
        sa_column=Column(
            DateTime(timezone=True),
            server_default=func.now(),
            nullable=False,
        ),
        default=None,
    )
    is_final_session: bool = Field(
        sa_column=Column(Boolean, nullable=False, default=False)
    )
    status: SessionStatus = Field(
        sa_column=Column(
            Enum(SessionStatus, values_callable=lambda e: [m.value for m in e]),
            nullable=False,
        )
    )

    study_circle: Optional["StudyCircle"] = Relationship(back_populates="sessions")
    event: Optional["Event"] = Relationship(back_populates="study_circle_sessions")
    attendance_records: List["StudyCircleAttendance"] = Relationship(back_populates="session")


class StudyCircleAttendance(SQLModel, table=True):
    """Represents an attendance record for one member in one session."""

    __tablename__ = "studycircleattendance"
    __table_args__ = (
        UniqueConstraint(
            "session_id", "study_circle_member_id", name="unique_session_attendance"
        ),
    )

    id: int = Field(sa_column=Column(Integer, primary_key=True, autoincrement=True))
    session_id: int = Field(
        sa_column=Column(Integer, ForeignKey("studycirclesession.id"), nullable=False)
    )
    study_circle_member_id: int = Field(
        sa_column=Column(Integer, ForeignKey("studycirclemember.id"), nullable=False)
    )
    role: AttendanceRole = Field(
        sa_column=Column(
            Enum(AttendanceRole, values_callable=lambda e: [m.value for m in e]),
            nullable=False,
        )
    )
    attended: bool = Field(sa_column=Column(Boolean, nullable=False, default=False))
    session: Optional["StudyCircleSession"] = Relationship(back_populates="attendance_records")
    member: Optional["StudyCircleMember"] = Relationship(back_populates="attendance_records")