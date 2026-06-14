# __author__ = Issa Masumbuko

"""Pydantic models for person-facing endpoints."""

from typing import Optional
from pydantic import BaseModel


class CreatePersonRequest(BaseModel):
    """Payload for adding a new person into the database."""
    name: str
    gender: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    coordinator_role: Optional[str] = None
    date_of_birth: Optional[str] = None  


class UpdatePersonRequest(BaseModel):
    """Payload for updating an existing person's information."""
    name: Optional[str] = None
    gender: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    coordinator_role: Optional[str] = None
    date_of_birth: Optional[str] = None


class PersonResponse(BaseModel):
    """Lightweight person info used in list views and nested responses."""
    id: int
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    gender: Optional[str] = None


class PersonDetailResponse(BaseModel):
    """Full profile view for a selected participant."""
    id: int
    name: str
    gender: Optional[str] = None
    date_of_birth: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    coordinator_role: Optional[str] = None
    guardians: list["GuardianSummary"] = []
    course_progressions: list["CourseProgressionSummary"] = []
    event_history: list["EventHistorySummary"] = []


# Inline sub-models used only inside PersonDetailResponse.

class GuardianSummary(BaseModel):
    """Guardian info as seen from a person's profile."""
    id: int
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    relationship: str 


class CourseProgressionSummary(BaseModel):
    """A person's status on a single course, as seen from their profile."""
    course_id: int
    course_name: str
    course_title: str
    status: str  


class EventHistorySummary(BaseModel):
    """Summary of one event a person participated in, as seen from their profile."""
    event_id: int
    event_name: str
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    roles: list[str] = []
    attendance_status: Optional[str] = None
    overnight_status: Optional[str] = None


PersonDetailResponse.model_rebuild()