# __author__ = Issa Masumbuko

"""Pydantic models for orientation-related endpoints."""

from typing import Optional
from pydantic import BaseModel

from tables.orientation import OrientationGroupStatus, OrientationParticipantRole


class GenerateOrientationGroupsRequest(BaseModel):
    """Payload for triggering automatic orientation-group generation."""
    min_participants: Optional[int] = None
    max_participants: Optional[int] = None
    min_facilitators: int = 1


class OrientationGroupAssignmentRequest(BaseModel):
    """Payload for assigning or reassigning a single participant to an orientation group."""
    participant_id: int
    group_id: int
    role: OrientationParticipantRole


class UpdateOrientationGroupRequest(BaseModel):
    """Payload for updating an orientation group's name or status."""
    name: Optional[str] = None
    status: Optional[OrientationGroupStatus] = None


class OrientationParticipantResponse(BaseModel):
    """A participant's membership record within an orientation group."""
    orientation_participant_id: int
    participant_id: int
    name: str
    role: OrientationParticipantRole


class OrientationGroupResponse(BaseModel):
    """Full orientation group detail."""
    id: int
    name: str
    status: OrientationGroupStatus
    facilitators: list[OrientationParticipantResponse] = []
    participants: list[OrientationParticipantResponse] = []


class OrientationGroupSummary(BaseModel):
    """Slim orientation group info used inside EventDetailResponse."""
    id: int
    name: str
    status: OrientationGroupStatus
    facilitator_count: int
    participant_count: int