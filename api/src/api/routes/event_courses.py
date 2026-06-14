# __author__ = Issa Masumbuko

from fastapi import APIRouter
from coordinatetbi.tables.event_course import (
    EventCourse,    
)

# form ..models import 

router = APIRouter(
    prefix="/events/{event_id}/courses",
    tags=["Event Courses"],
)

# ---- Event Books CRUD ----
@router.post("/",
    summary="Create a new event course",
    response_description="The created event course details",
)
def add_course_to_event(event_id: int):
    ...

@router.patch("/{course_id}",
    summary="Update a specific event course",
    response_description="The updated details of a specific event course",
)
def update_event_course(event_id: int, course_id: int):
    ...

@router.get("/",
    summary="Get a list of all courses for a specific event",
    response_description="Returns a list of all courses for a specific event in the database",
)
def list_event_courses(event_id: int):
    ...

@router.get("/{course_id}",
    summary="Get a specific event course",
    response_description="Returns the details of a specific event course",
)
def get_event_course(event_id: int, course_id: int):
    ...

@router.delete("/{course_id}",
    summary="Delete a specific event course",
    response_description="Deletes a specific event course from the database",
)
def delete_event_course(event_id: int, course_id: int):
    ...