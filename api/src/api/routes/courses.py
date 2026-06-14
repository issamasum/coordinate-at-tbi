# __author__ = Issa Masumbuko
from fastapi import APIRouter, Body, HTTPException

from coordinatetbi.tables.course import (
    Course,
)

# from ..models import ()

router = APIRouter(
    prefix="/courses",
    tags=["Courses"],
)

# ---- Courses CRUD ----
@router.post("/",
    summary="Create a new course",
    response_description="The created course details",
)
def create_course():
    ...

@router.patch("/{course_id}",
    summary="Update a specific course",
    response_description="The updated details of a specific course",
)
def update_course(course_id: int):
    ...

@router.get("/",
    summary="Get a list of all courses",
    response_description="Returns a list of all courses in the database",
)
def list_courses():
    ... 

@router.get("/{course_id}",
    summary="Get a specific course",
    response_description="Returns the details of a specific course",
)
def get_course(course_id: int):
    ... 

@router.delete("/{course_id}",
    summary="Delete a specific course",
    response_description="Deletes a specific course from the database",
)
def delete_course(course_id: int):
    ...
