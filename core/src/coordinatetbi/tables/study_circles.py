# __author__ = Issa Masumbuko

"""Database-backed all the study circle models"""
import enum
from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, Text, ForeignKey, UniqueConstraint
from sqlmodel import (
    Field, 
    SQLModel,
    func,
    Enum,
)

class StudyCircleStatus(str, enum.Enum):
    """Enumeration for study circle status designations."""
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
    """Represents a study circle organized by the Triangle Baha'i Institute."""

    __tablename__ = "studycircle"
    __table_args__ = (
        UniqueConstraint("name", "event_created_at_id", name="unique_study_circle_name_event"),
    )

    id: int = Field(
        sa_column=Column(Integer, primary_key=True, autoincrement=True)
    )
    name: str = Field(
            sa_column=Column(Text, nullable=False)
    )
    status: StudyCircleStatus = Field(
        sa_column=Column(
            Enum(StudyCircleStatus, values_callable=lambda e: [m.value for m in e]),
            nullable=False
        )
    )
    course_id: int = Field(
        sa_column=Column(Integer, ForeignKey("course.name"), nullable=False)
    )
    event_created_at_id: int = Field(
        sa_column=Column(Integer, ForeignKey("event.id"), nullable=True)
    )


class StudyCircleMember(SQLModel, table=True):
    """Represents a member of a study circle organized by the Triangle Baha'i Institute."""

    __tablename__ = "studycirclemember"

    id: int = Field(
        sa_column=Column(Integer, primary_key=True, autoincrement=True)
    )
    study_circle_id: int = Field(
        sa_column=Column(Integer, ForeignKey("study_circle.id"), nullable=False)
    )
    person_id: int = Field(
        sa_column=Column(Integer, ForeignKey("person.id"), nullable=False)
    )
    status: MemberStatus = Field(
        sa_column=Column(
            Enum(MemberStatus, values_callable=lambda e: [m.value for m in e]),
            nullable=False
        )
    )


class StudyCircleSession(SQLModel, table=True):
    """Represents a study circle session or meeting."""

    __tablename__ = "studycirclesession"

    id: int = Field(
        sa_column=Column(Integer, primary_key=True, autoincrement=True)
    )
    study_circle_id: int = Field(
        sa_column=Column(Integer, ForeignKey("studycircle.id"), nullable=False)
    )
    event_id: int = Field(
        sa_column=Column(Integer, ForeignKey("event.id"), nullable=True)
    )
    session_number: int = Field(
        sa_column=Column(Integer, nullable=False)   
    )
    session_date: datetime = Field(
        sa_column=Column(
            DateTime(timezone=True),
            server_default=func.now(),
            onupdate=func.now(),
            nullable=False,
        ),
        default=None,
    )
    final_session: bool = Field()
    status: SessionStatus = Field(
        sa_column=Column(
            Enum(SessionStatus, values_callable=lambda e: [m.value for m in e]),
            nullable=False
        )
    )



class StudyCircleAttendance(SQLModel, table=True):
    """Represents a study circle  attendance record for a member of a study circle."""

    __tablename__ = "studycircleattendance"

    id: int = Field(
        sa_column=Column(Integer, primary_key=True, autoincrement=True)
    )
    session_id: int = Field(
        sa_column=Column(Integer, ForeignKey("studycirclesession.id"), nullable=False)
    )
    study_circle_member_id: int = Field(
        sa_column=Column(Integer, ForeignKey("studycirclemember.id"), nullable=False)
    )
    role: AttendanceRole = Field(
        sa_column=Column(
            Enum(AttendanceRole, values_callable=lambda e: [m.value for m in e]),
            nullable=False
        )
    )
    attended: bool = Field()