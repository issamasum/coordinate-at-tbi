# __author__ = Issa Masumbuko

"""Pydantic models for course and course-progression endpoints."""

from pydantic import BaseModel
from typing import Optional

from tables.course_progression import CourseProgressionStatus


# ---- Course models ----

class CreateCourseRequest(BaseModel):
    """Payload for creating a new course."""
    name: str
    title: str
    description: Optional[str] = None


class UpdateCourseRequest(BaseModel):
    """Payload for updating an existing course."""
    name: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None


class CourseResponse(BaseModel):
    """A single Ruhi Institute course/book."""
    id: int
    name: str
    title: str
    description: Optional[str] = None


class EventCourseRequest(BaseModel):
    """Payload for setting the courses offered at an event."""
    course_ids: list[int]


# ---- Course progression models ----

class CourseProgressionItem(BaseModel):
    """A single course + status pair within a progression request."""
    course_id: int
    status: CourseProgressionStatus


class CourseProgressionsRequest(BaseModel):
    """Payload for creating or updating one or more course progressions for a person."""
    person_id: int
    progressions: list[CourseProgressionItem]


class CourseProgressionResponse(BaseModel):
    """A person's status on a single course."""
    id: int
    person_id: int
    course_id: int
    course_name: str
    course_title: str
    status: CourseProgressionStatus


class PersonProgressionSummary(BaseModel):
    """Summary of one person's progression, as seen from a course view."""
    person_id: int
    person_name: str
    status: CourseProgressionStatus