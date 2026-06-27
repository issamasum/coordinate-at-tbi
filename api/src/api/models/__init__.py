# __author__ = Issa Masumbuko

"""package — single import surface for all Pydantic models."""

from .person import (
    Gender,
    CoordinatorRole,
    CreatePersonRequest,
    UpdatePersonRequest,
    PersonResponse,
    PersonDetailResponse,
    EventHistorySummary,
    CourseProgressionSummary,
    GuardianSummary,
)
from .guardian import (
    CreateGuardianRequest,
    UpdateGuardianRequest,
    LinkGuardianRequest,
    GuardianResponse,
)
from .cottage import (
    CreateCottageRequest,
    UpdateCottageRequest,
    CottageResponse,
)
from .dorm import (
    CreateDormRequest,
    UpdateDormRequest,
    DormResponse,
    ActivateDormRoomsRequest,
    GenerateDormAssignmentsRequest,
    DormAssignmentRequest,
    UpdateDormAssignmentRequest,
    EventDormRoomResponse,
    DormAssignmentResponse,
)
from .orientation import (
    GenerateOrientationGroupsRequest,
    OrientationGroupAssignmentRequest,
    UpdateOrientationGroupRequest,
    OrientationParticipantResponse,
    OrientationGroupResponse,
    OrientationGroupSummary,
)
from .course import (
    CourseProgressionStatus,
    CreateCourseRequest,
    UpdateCourseRequest,
    CourseResponse,
    EventCourseRequest,
    CourseProgressionItem,
    CourseProgressionsRequest,
    CourseProgressionResponse,
    PersonProgressionSummary,
)
from .event import (
    CreateEventRequest,
    UpdateEventRequest,
    EventResponse,
    EventDetailResponse,
    AddEventParticipantsRequest,
    UpdateEventParticipantRequest,
    EventParticipantResponse,
)
from .study_circle import (
    CreateStudyCircleRequest,
    UpdateStudyCircleRequest,
    CreateSessionRequest,
    UpdateSessionRequest,
    AddMemberRequest,
    UpdateStudyCircleMemberRequest,
    AttendanceRecordRequest,
    SessionAttendanceRecordRequest,
    StudyCircleMemberResponse,
    StudyCircleResponse,
    StudyCircleSummary,
)

__all__ = [
    # Person
    "Gender",
    "CoordinatorRole",
    "CreatePersonRequest",
    "UpdatePersonRequest",
    "PersonResponse",
    "PersonDetailResponse",
    "EventHistorySummary",
    "CourseProgressionSummary",
    "GuardianSummary",
    # Guardian
    "CreateGuardianRequest",
    "UpdateGuardianRequest",
    "LinkGuardianRequest",
    "GuardianResponse",
    # Cottage
    "CreateCottageRequest",
    "UpdateCottageRequest",
    "CottageResponse",
    # Dorm
    "CreateDormRequest",
    "UpdateDormRequest",
    "DormResponse",
    "ActivateDormRoomsRequest",
    "GenerateDormAssignmentsRequest",
    "DormAssignmentRequest",
    "UpdateDormAssignmentRequest",
    "EventDormRoomResponse",
    "DormAssignmentResponse",
    # Orientation
    "GenerateOrientationGroupsRequest",
    "OrientationGroupAssignmentRequest",
    "UpdateOrientationGroupRequest",
    "OrientationParticipantResponse",
    "OrientationGroupResponse",
    "OrientationGroupSummary",
    # Course
    "CourseProgressionStatus",
    "CreateCourseRequest",
    "UpdateCourseRequest",
    "CourseResponse",
    "EventCourseRequest",
    "CourseProgressionItem",
    "CourseProgressionsRequest",
    "CourseProgressionResponse",
    "PersonProgressionSummary",
    # Event
    "CreateEventRequest",
    "UpdateEventRequest",
    "EventResponse",
    "EventDetailResponse",
    "AddEventParticipantsRequest",
    "UpdateEventParticipantRequest",
    "EventParticipantResponse",
    # Study Circle
    "CreateStudyCircleRequest",
    "UpdateStudyCircleRequest",
    "CreateSessionRequest",
    "UpdateSessionRequest",
    "AddMemberRequest",
    "UpdateStudyCircleMemberRequest",
    "AttendanceRecordRequest",
    "SessionAttendanceRecordRequest",
    "StudyCircleMemberResponse",
    "StudyCircleResponse",
    "StudyCircleSummary",
]