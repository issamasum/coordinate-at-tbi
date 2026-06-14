# __author__ = Issa Masumbuko

"""Pydantic models for dorm-related endpoints."""

from typing import Optional
from pydantic import BaseModel

from tables.dorm import DormAssignmentStatus
from tables.event import DormStrategy


class ActivateDormRoomsRequest(BaseModel):
    """Payload for activating one or more dorm rooms for an event in bulk."""
    dorm_ids: list[int]


class DeactivateDormRoomsRequest(BaseModel):
    """Payload for deactivating dorm rooms for an event in bulk."""
    event_dorm_room_ids: list[int] 


class GenerateDormAssignmentsRequest(BaseModel):
    """Payload for triggering the automatic dorm-assignment algorithm."""
    strategy: Optional[DormStrategy] = None 
    respect_previous_history: bool = True


class DormAssignmentRequest(BaseModel):
    """A single participant-to-room mapping used in bulk requests."""
    participant_id: int       
    event_dorm_room_id: int 


class BulkDormAssignmentRequest(BaseModel):
    """Payload for manually assigning multiple participants to rooms at once."""
    assignments: list[DormAssignmentRequest]


class UpdateDormAssignmentRequest(BaseModel):
    """Payload for moving a single participant to a different room or changing their status."""
    event_dorm_room_id: Optional[int] = None
    status: Optional[DormAssignmentStatus] = None


class BulkUpdateDormAssignmentStatusRequest(BaseModel):
    """Payload for confirming or canceling multiple assignments at once """
    assignment_ids: list[int] 
    status: DormAssignmentStatus


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