# __author__ = Issa Masumbuko

from fastapi import APIRouter
from coordinatetbi.tables.study_circle import (
    StudyCircle,
    StudyCircleMember,
    StudyCircleSession,
    StudyCircleAttendance,
)

router = APIRouter(
    prefix="/study-circles",
    tags=["Study Circles"],
)   

# ---- Study Circles CRUD ----

@router.post("/",
    summary="Create a new study circle",
    response_description="The created study circle details",
)
def create_study_circle():
    ...

@router.patch("/{study_circle_id}",
    summary="Update a specific study circle",
    response_description="The updated details of a specific study circle",
)
def update_study_circle(study_circle_id: int):
    ... 

@router.get("/",
    summary="Get a list of all study circles",
    response_description="Returns a list of all study circles in the database",
)
def list_study_circles():
    ...

@router.get("/{study_circle_id}",
    summary="Get a specific study circle",
    response_description="Returns the details of a specific study circle",
)
def get_study_circle(study_circle_id: int):
    ... 

@router.delete("/{study_circle_id}",
    summary="Delete a specific study circle",
    response_description="Deletes a specific study circle from the database",
)
def delete_study_circle(study_circle_id: int):
    ...


# ---- Study Circle Members CRUD ----

member_prefix = "/{study_circle_id}/members"

@router.post(member_prefix + "/",
    summary="Add a member to a study circle",
    response_description="The created study circle member details",
)
def add_member_to_study_circle(study_circle_id: int):
    ...

@router.patch(member_prefix + "/{member_id}",
    summary="Update a specific study circle member",
    response_description="The updated details of a specific study circle member",
)
def update_study_circle_member(study_circle_id: int, member_id: int):
    ...

@router.get(member_prefix + "/",
    summary="Get a list of all members in a study circle",
    response_description="Returns a list of all members in a specific study circle",
)
def list_members_in_study_circle(study_circle_id: int):
    ...

@router.get(member_prefix + "/{member_id}",
    summary="Get a specific study circle member",
    response_description="Returns the details of a specific study circle member",
)
def get_study_circle_member(study_circle_id: int, member_id: int):
    ... 

@router.delete(member_prefix + "/{member_id}",
    summary="Delete a specific study circle member",
    response_description="Deletes a specific study circle member from the database",
)
def delete_study_circle_member(study_circle_id: int, member_id: int):
    ... 


# ---- Study Circle Sessions CRUD ----
session_prefix = "/{study_circle_id}/sessions"  

@router.post(session_prefix + "/",
    summary="Create a new study circle session",
    response_description="The created study circle session details",
)
def create_study_circle_session(study_circle_id: int):
    ... 

@router.patch(session_prefix + "/{session_id}",
    summary="Update a specific study circle session",
    response_description="The updated details of a specific study circle session",
)
def update_study_circle_session(study_circle_id: int, session_id: int):
    ... 

@router.get(session_prefix + "/",
    summary="Get a list of all sessions in a study circle",
    response_description="Returns a list of all sessions in a specific study circle",
)
def list_sessions_in_study_circle(study_circle_id: int):
    ...

@router.get(session_prefix + "/{session_id}",
    summary="Get a specific study circle session",
    response_description="Returns the details of a specific study circle session",
)
def get_study_circle_session(study_circle_id: int, session_id: int):
    ...

@router.delete(session_prefix + "/{session_id}",
    summary="Delete a specific study circle session",
    response_description="Deletes a specific study circle session from the database",
)
def delete_study_circle_session(study_circle_id: int, session_id: int):
    ...

# auto generate a session for the study circle
@router.post("/events/{event_id}/study-circles/sessions/auto",
    summary="Auto-generate a study circle session for an event",
    response_description="The created study circle session details",
)
def generate_study_circle_session_for_event(event_id: int):
    ... 



# ---- Study Circle Attendance CRUD ----
attendance_prefix = "/{study_circle_id}/sessions/{session_id}/attendance"

@router.post(attendance_prefix + "/",
    summary="Record attendance for a study circle session",
    response_description="The created study circle attendance details",
)
def record_study_circle_attendance(study_circle_id: int, session_id: int):
    ...

@router.patch(attendance_prefix + "/{attendance_id}",
    summary="Update a specific study circle attendance record",
    response_description="The updated details of a specific study circle attendance record",
)
def update_study_circle_attendance(study_circle_id: int, session_id: int, attendance_id: int):
    ...

@router.get(attendance_prefix + "/",
    summary="Get a list of all attendance records for a study circle session",
    response_description="Returns a list of all attendance records for a specific study circle session",
)
def list_attendance_records_for_study_circle_session(study_circle_id: int, session_id: int):
    ...

@router.get(attendance_prefix + "/{attendance_id}",
    summary="Get a specific study circle attendance record",
    response_description="Returns the details of a specific study circle attendance record",
)
def get_study_circle_attendance(study_circle_id: int, session_id: int, attendance_id: int):
    ...

@router.delete(attendance_prefix + "/{attendance_id}",
    summary="Delete a specific study circle attendance record",
    response_description="Deletes a specific study circle attendance record from the database",
)
def delete_study_circle_attendance(study_circle_id: int, session_id: int, attendance_id: int):
    ...
