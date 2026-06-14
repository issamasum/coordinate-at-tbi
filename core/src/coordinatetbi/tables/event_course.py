# __author__ = Issa Masumbuko

"""Database-backed event-course join models"""

from typing import TYPE_CHECKING, Optional

from sqlalchemy import Column, ForeignKey, Integer, UniqueConstraint
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .event import Event
    from .course import Course


class EventCourse(SQLModel, table=True):
    """Represents a course offered at a specific event."""

    __tablename__ = "eventcourse"
    __table_args__ = (
        UniqueConstraint("course_id", "event_id", name="unique_event_course"),
    )

    id: int = Field(sa_column=Column(Integer, primary_key=True, autoincrement=True))
    course_id: int = Field(
        sa_column=Column(Integer, ForeignKey("course.id"), nullable=False)
    )
    event_id: int = Field(
        sa_column=Column(Integer, ForeignKey("event.id"), nullable=False)
    )
    course: Optional["Course"] = Relationship(back_populates="event_courses")
    event: Optional["Event"] = Relationship(back_populates="event_courses")
