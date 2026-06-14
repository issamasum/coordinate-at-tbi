# __author__ = Issa Masumbuko

"""Database-backed models for course progression"""

import enum
from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlalchemy import Column, DateTime, ForeignKey, Integer, UniqueConstraint
from sqlmodel import Field, Relationship, SQLModel, func, Enum

if TYPE_CHECKING:
    from .person import Person
    from .course import Course


class CourseProgressionStatus(str, enum.Enum):
    NOT_STARTED = "Not Started"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"


class CourseProgression(SQLModel, table=True):
    """Represents a person's progression through a Ruhi Institute Course."""

    __tablename__ = "courseprogression"
    __table_args__ = (
        UniqueConstraint("person_id", "course_id", name="unique_person_course_progression"),
    )

    id: int = Field(sa_column=Column(Integer, primary_key=True, autoincrement=True))
    person_id: int = Field(
        sa_column=Column(Integer, ForeignKey("person.id"), nullable=False)
    )
    course_id: int = Field(
        sa_column=Column(Integer, ForeignKey("course.id"), nullable=False)
    )
    status: CourseProgressionStatus = Field(
        sa_column=Column(
            Enum(CourseProgressionStatus, values_callable=lambda e: [m.value for m in e]),
            nullable=False,
        )
    )
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False),
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
    person: Optional["Person"] = Relationship(back_populates="course_progressions")
    course: Optional["Course"] = Relationship(back_populates="progressions")