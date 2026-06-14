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


# Event participants Models


class AddEventParticipantsRequest(BaseModel):
    """Payload for adding one or more participants to an event.
    Used for uploading a roster. 
    """
    person_ids: list[int]


class RemoveEventParticipantsRequest(BaseModel):
    """Payload for removing one or more participants from an event in bulk."""
    participant_ids: list[int]  


class UpdateParticipantRolesRequest(BaseModel):
    """Payload for setting all roles of a single participant.
    """
    roles: list[ParticipantRole]


class ParticipantRoleUpdate(BaseModel):
    participant_id: int  
    roles: list[ParticipantRole]


class BulkUpdateParticipantRolesRequest(BaseModel):
    """Payload for updating roles for multiple participants at once."""
    updates: list[ParticipantRoleUpdate]


class AttendanceUpdate(BaseModel):
    """A single attendance record used in bulk requests and single-participant updates."""
    participant_id: int  
    attendance_status: AttendanceStatus


class BulkAttendanceUpdateRequest(BaseModel):
    """Payload for marking attendance for multiple participants at once."""
    updates: list[AttendanceUpdate]


class OvernightUpdate(BaseModel):
    """A single overnight record used in bulk requests and single-participant updates."""
    participant_id: int
    overnight_status: OvernightStatus


class BulkUpdateOvernightRequest(BaseModel):
    """Payload for updating overnight status for multiple participants at once."""
    updates: list[OvernightUpdate]


class EventParticipantResponse(BaseModel):
    """Response model for a single event participant record."""
    participant_id: int
    event_id: int
    participant_name: str
    roles: list[ParticipantRole]
    attendance_status: Optional[AttendanceStatus] = None
    overnight_status: Optional[OvernightStatus] = None