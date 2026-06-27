# __author__ = Issa Masumbuko

from typing import Annotated

from fastapi import APIRouter, Body

from ..models import (
    CreateCourseRequest,
    UpdateCourseRequest,
    CourseResponse,
)

router = APIRouter(
    prefix="/courses",
    tags=["Courses"],
)

# ---- Courses CRUD ----

@router.post("/",
    summary="Create a new course",
    response_description="The created course details",
)
def create_course(body: Annotated[CreateCourseRequest, Body()]) -> CourseResponse:
    """Creates a new course with the given details.

    args:
        body: The details of the course to create

    returns:
        The details of the created course
    """
    ...


@router.get("/",
    summary="Get a list of all courses",
    response_description="Returns a list of all courses in the database",
)
def list_courses() -> list[CourseResponse]:
    """Returns a list of all courses in the database.

    returns:
        A list of all courses in the database
    """
    ...


@router.get("/{course_id}",
    summary="Get a specific course",
    response_description="Returns the details of a specific course",
)
def get_course(course_id: int) -> CourseResponse:
    """Returns the details of a specific course.

    args:
        course_id: The ID of the course to retrieve

    returns:
        The details of the requested course
    """
    ...


@router.patch("/{course_id}",
    summary="Update a specific course",
    response_description="The updated details of a specific course",
)
def update_course(
    course_id: int,
    body: Annotated[UpdateCourseRequest, Body()],
) -> CourseResponse:
    """Updates the details of a specific course.

    args:
        course_id: The ID of the course to update
        body: The fields to update on the course

    returns:
        The updated details of the course
    """
    ...


@router.delete("/{course_id}",
    summary="Delete a specific course",
    response_description="Confirmation of course deletion",
)
def delete_course(course_id: int) -> None:
    """Deletes a specific course from the database.

    args:
        course_id: The ID of the course to delete
    """
    ...