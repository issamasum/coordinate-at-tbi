# __author__ = Issa Masumbuko

"""Pydantic models for study-circle endpoints."""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel

from tables.study_circle import StudyCircleStatus, MemberStatus, SessionStatus, AttendanceRole


class CreateStudyCircleRequest(BaseModel):
    """Payload for creating a new study circle."""
    name: str
    course_id: int
    event_id: Optional[int] = None
    status: StudyCircleStatus = StudyCircleStatus.IN_PROGRESS


class UpdateStudyCircleRequest(BaseModel):
    """Payload for updating a study circle's metadata or status."""
    name: Optional[str] = None
    status: Optional[StudyCircleStatus] = None
    course_id: Optional[int] = None


class AddMemberRequest(BaseModel):
    """Payload for adding a single member to a study circle."""
    person_id: int
    role: AttendanceRole
    status: MemberStatus = MemberStatus.ACTIVE


class UpdateStudyCircleMemberRequest(BaseModel):
    """Payload for updating a single member's status (e.g. mark as dropped)."""
    status: MemberStatus


class CreateSessionRequest(BaseModel):
    """Payload for logging a new session of a study circle."""
    session_number: int
    session_date: datetime
    is_final_session: bool = False
    status: SessionStatus = SessionStatus.DRAFT
    event_id: Optional[int] = None


class UpdateSessionRequest(BaseModel):
    """Payload for updating a session's details or status."""
    session_date: Optional[datetime] = None
    is_final_session: Optional[bool] = None
    status: Optional[SessionStatus] = None


class AttendanceRecordRequest(BaseModel):
    """A single member's attendance entry for one session."""
    member_id: int
    attended: bool
    role: AttendanceRole


class SessionAttendanceRecordRequest(BaseModel):
    """Payload for recording attendance for an entire session at once."""
    records: list[AttendanceRecordRequest]


class StudyCircleMemberResponse(BaseModel):
    """A member's record within a study circle."""
    id: int
    person_id: int
    name: str
    role: AttendanceRole
    status: MemberStatus


class StudyCircleResponse(BaseModel):
    """Full study circle detail."""
    id: int
    name: str
    status: StudyCircleStatus
    course_id: int
    course_name: str
    event_id: Optional[int] = None
    members: list[StudyCircleMemberResponse] = []


class StudyCircleSummary(BaseModel):
    """Slim study circle info used inside EventDetailResponse."""
    id: int
    name: str
    status: StudyCircleStatus
    course_name: str
    member_count: int