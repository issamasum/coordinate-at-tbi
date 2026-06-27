# __author__ = Issa Masumbuko

"""Pydantic models for event-related endpoints."""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel

from tables.event import EventStatus, DormStrategy
from tables.event_participant import OvernightStatus, AttendanceStatus, ParticipantRole

from .person import PersonResponse
from .study_circle import StudyCircleSummary
from .orientation import OrientationGroupSummary
from .dorm import DormAssignmentResponse


# ---- Event models ----

class CreateEventRequest(BaseModel):
    """Payload for creating a new event."""
    name: str
    location: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    overnight: bool = False
    dorm_strategy: Optional[DormStrategy] = None


class UpdateEventRequest(BaseModel):
    """Payload for updating an existing event."""
    name: Optional[str] = None
    location: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    overnight: Optional[bool] = None
    dorm_strategy: Optional[DormStrategy] = None
    status: Optional[EventStatus] = None


class EventResponse(BaseModel):
    """Lightweight event info used in list views."""
    id: int
    name: str
    location: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    status: Optional[EventStatus] = None
    overnight: Optional[bool] = None


class EventDetailResponse(BaseModel):
    """Full event detail."""
    id: int
    name: str
    location: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    overnight: Optional[bool] = None
    dorm_strategy: Optional[DormStrategy] = None
    status: Optional[EventStatus] = None
    participants: list[PersonResponse] = []
    study_circles: list[StudyCircleSummary] = []
    orientation_groups: list[OrientationGroupSummary] = []
    dorm_assignments: list[DormAssignmentResponse] = []


# ---- Event participant models ----

class AddEventParticipantsRequest(BaseModel):
    """Payload for adding one or more participants to an event."""
    person_ids: list[int]


class UpdateEventParticipantRequest(BaseModel):
    """Payload for updating a single participant's roles, attendance, or overnight status.
    Only fields that are set will be updated.
    """
    roles: Optional[list[ParticipantRole]] = None
    attendance_status: Optional[AttendanceStatus] = None
    overnight_status: Optional[OvernightStatus] = None


class EventParticipantResponse(BaseModel):
    """Response model for a single event participant record."""
    participant_id: int
    event_id: int
    participant_name: str
    roles: list[ParticipantRole]
    attendance_status: Optional[AttendanceStatus] = None
    overnight_status: Optional[OvernightStatus] = None