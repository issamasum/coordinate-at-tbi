# __author__ = Issa Masumbuko

"""Pydantic models for dorm-related endpoints."""

from typing import Optional
from pydantic import BaseModel

from tables.dorm import DormAssignmentStatus
from tables.event import DormStrategy


# ---- Dorm models ----

class CreateDormRequest(BaseModel):
    """Payload for creating a new dorm room inside a cottage."""
    name: str
    capacity: int


class UpdateDormRequest(BaseModel):
    """Payload for updating an existing dorm room."""
    name: Optional[str] = None
    capacity: Optional[int] = None


class DormResponse(BaseModel):
    """A single dorm room record."""
    id: int
    name: str
    capacity: int
    cottage_id: int
    cottage_name: str


# ---- Event dorm room models ----

class ActivateDormRoomsRequest(BaseModel):
    """Payload for activating one or more dorm rooms for an event."""
    room_ids: list[int]


class GenerateDormAssignmentsRequest(BaseModel):
    """Payload for triggering the automatic dorm-assignment algorithm."""
    strategy: Optional[DormStrategy] = None
    respect_previous_history: bool = True


class DormAssignmentRequest(BaseModel):
    """Payload for manually assigning a single participant to a room."""
    participant_id: int
    event_dorm_room_id: int


class UpdateDormAssignmentRequest(BaseModel):
    """Payload for moving a participant to a different room or changing their status."""
    event_dorm_room_id: Optional[int] = None
    status: Optional[DormAssignmentStatus] = None


class EventDormRoomResponse(BaseModel):
    """A dorm room activated for a specific event."""
    id: int
    dorm_id: int
    dorm_name: str
    cottage_name: str
    cottage_gender: str
    capacity: int
    assigned_count: int


class DormAssignmentResponse(BaseModel):
    """A single participant's dorm assignment."""
    assignment_id: int
    participant_id: int
    participant_name: str
    event_dorm_room_id: int
    dorm_name: str
    cottage_name: str
    status: DormAssignmentStatus