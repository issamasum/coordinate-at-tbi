# __author__ = Issa Masumbuko

"""Database-backed course models"""

from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import Column, Integer, Text, UniqueConstraint
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .course_progression import CourseProgression
    from .event_course import EventCourse
    from .study_circle import StudyCircle


class Course(SQLModel, table=True):
    """Represents a Ruhi Institute Course."""

    __tablename__ = "course"
    __table_args__ = (
        UniqueConstraint("name", name="unique_course_name"),
        UniqueConstraint("title", name="unique_course_title"),
    )

    id: int = Field(sa_column=Column(Integer, primary_key=True, autoincrement=True))
    name: str = Field(sa_column=Column(Text, nullable=False))
    title: str = Field(sa_column=Column(Text, nullable=False))
    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))
    event_courses: List["EventCourse"] = Relationship(back_populates="course")
    progressions: List["CourseProgression"] = Relationship(back_populates="course")
    study_circles: List["StudyCircle"] = Relationship(back_populates="course")