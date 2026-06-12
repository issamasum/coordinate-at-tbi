# __author__ = Issa Masumbuko

"""Database-backed event-course join models"""


from sqlalchemy import Column, Integer, ForeignKey
from sqlmodel import (
    Field, 
    SQLModel,
    UniqueConstraint,
)

class EventCourse(SQLModel, table=True):
    """Represents a course offered at an event organized by the Triangle Baha'i Institute."""

    __tablename__ = "eventcourse"
    __table_args__ = (
        UniqueConstraint("course_id", "event_id", name="unique_event_course"),
    )

    id: int = Field(
        sa_column=Column(Integer, primary_key=True, autoincrement=True)
    )
    course_id: int = Field(
        sa_column=Column(Integer, ForeignKey("course.id"), nullable=False)
    )
    event_id: int = Field(
        sa_column=Column(Integer, ForeignKey("event.id"), nullable=False)
    )
