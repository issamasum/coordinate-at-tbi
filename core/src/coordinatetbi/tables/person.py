# __author__ = Issa Masumbuko

"""Database-backed people models"""

import enum
from datetime import datetime
from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import Column, DateTime, Integer, Text
from sqlmodel import Field, Relationship, SQLModel, func, Enum

if TYPE_CHECKING:
    from .guardian import Guardian
    from .user import User
    from .course_progression import CourseProgression
    from .event import EventParticipant
    from .study_circle import StudyCircleMember


class CoordinatorRole(str, enum.Enum):
    MAIN_COORDINATOR = "main coordinator"
    ASSISTANT_COORDINATOR = "assistant coordinator"


class Gender(str, enum.Enum):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"


class Person(SQLModel, table=True):
    """Represents a person involved with the Triangle Baha'i Institute activities."""

    __tablename__ = "person"

    id: int = Field(
        sa_column=Column(
            Integer, 
            primary_key=True, 
            autoincrement=True
            )
    )
    name: str = Field(
        sa_column=Column(
            Text, 
            nullable=False
            )
    )
    email: Optional[str] = Field(
        default=None, 
        sa_column=Column(
            Text, 
            nullable=True
            )
    )
    phone: Optional[str] = Field(
        default=None, 
        sa_column=Column(
            Text, 
            nullable=True
            )
    )
    adress: Optional[str] = Field(
        default=None, 
        sa_column=Column(
            Text, 
            nullable=True
            )
    )
    gender: Optional[Gender] = Field(
        default=None,
        sa_column=Column(
            Enum(Gender, values_callable=lambda e: [m.value for m in e]), nullable=True
        ),
    )
    coordinator_role: Optional[CoordinatorRole] = Field(
        default=None,
        sa_column=Column(
            Enum(CoordinatorRole, values_callable=lambda e: [m.value for m in e]),
            nullable=True,
        ),
    )
    date_of_birth: Optional[datetime] = Field(
        default=None, sa_column=Column(DateTime(timezone=False), nullable=True)
    )
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False),
        default=None,
    )
    deleted_at: Optional[datetime] = Field(
        default=None, sa_column=Column(DateTime(timezone=True), nullable=True)
    )
    user: Optional["User"] = Relationship(back_populates="person")
    guardians: List["Guardian"] = Relationship(
        back_populates="people",
        sa_relationship_kwargs={
            "secondary": "personguardian", "lazy": "select"
            },
    )
    course_progressions: List["CourseProgression"] = Relationship(back_populates="person")
    event_participations: List["EventParticipant"] = Relationship(back_populates="person")
    study_circle_memberships: List["StudyCircleMember"] = Relationship(back_populates="person")