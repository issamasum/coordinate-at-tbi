# __author__ = Issa Masumbuko

"""Database-backed models for course progression"""

from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, ForeignKey
from sqlmodel import (
    Field, 
    SQLModel,
    func,
    Enum,
)

class CourseProgressionStatus(str, Enum):
    """Enumeration for course progression status."""
    NOT_STARTED = "Not started"
    IN_PROGRESS = " In progress"
    COMPLETED = "Completed"

class CourseProgression(SQLModel, table=True):
    """Represents a person's progression through a course offered by the Triangle Baha'i Institute."""

    __tablename__ = "courseprogression"

    id: int = Field(
        sa_column=Column(Integer, primary_key=True, autoincrement=True)
    )
    person_id: int = Field(
        sa_column=Column(Integer, ForeignKey("person.id"), nullable=False)
    )
    course_id: int = Field(
        sa_column=Column(Integer, ForeignKey("course.name"), nullable=False)
    )
    status: CourseProgressionStatus = Field(
        sa_column=Column(
            Enum(CourseProgressionStatus, values_callable=lambda e: [m.value for m in e]),
            nullable=False
        )
    )
    last_updated: datetime = Field(
        sa_column=Column(
            DateTime,  
            nullable=False, 
            default=func.now(), 
            onupdate=func.now()
        )
    )