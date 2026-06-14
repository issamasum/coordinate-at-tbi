# __author__ = Issa Masumbuko

"""Pydantic models for course (book) and course-progression endpoints."""

from pydantic import BaseModel
from typing import Optional


class CourseResponse(BaseModel):
    """A single Ruhi Institute course/book."""
    id: int
    name: str
    title: str  
    description: Optional[str] = None


class EventCourseRequest(BaseModel):
    """Payload for setting the books offered at an event.
    """
    course_ids: list[int]


class RecordCourseProgressionRequest(BaseModel):
    """Payload for recording or updating a person's progression through a course."""
    course_id: int
    status: str  
    
class BulkUpsertCourseProgressionRequest(BaseModel):
    """Payload for updating multiple course progressions for one person at once
    """
    progressions: list[RecordCourseProgressionRequest]


class CourseProgressionResponse(BaseModel):
    """A person's status on a single course."""
    course_id: int
    course_name: str
    course_title: str
    status: str  