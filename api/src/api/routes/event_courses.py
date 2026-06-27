# __author__ = Issa Masumbuko

from typing import Annotated

from fastapi import APIRouter, Body

from ..models import (
    EventCourseRequest,
    CourseResponse,
)

router = APIRouter(
    prefix="/events/{event_id}/courses",
    tags=["Event Courses"],
)

# ---- Event Courses CRUD ----

@router.post("/",
    summary="Add courses to an event",
    response_description="The courses now associated with the event",
)
def add_courses_to_event(
    event_id: int,
    body: Annotated[EventCourseRequest, Body()],
) -> list[CourseResponse]:
    """Adds one or more courses to a specific event.

    args:
        event_id: The ID of the event to add courses to
        body: The IDs of the courses to add

    returns:
        The details of all courses now associated with the event
    """
    ...


@router.get("/",
    summary="Get a list of all courses for a specific event",
    response_description="Returns a list of all courses associated with a specific event",
)
def list_event_courses(event_id: int) -> list[CourseResponse]:
    """Returns all courses associated with a specific event.

    args:
        event_id: The ID of the event to list courses for

    returns:
        A list of all courses associated with the event
    """
    ...


@router.get("/{course_id}",
    summary="Get a specific course for an event",
    response_description="Returns the details of a specific course in an event",
)
def get_event_course(event_id: int, course_id: int) -> CourseResponse:
    """Returns the details of a specific course associated with an event.

    args:
        event_id: The ID of the event
        course_id: The ID of the course to retrieve

    returns:
        The details of the requested course
    """
    ...


@router.delete("/{course_id}",
    summary="Remove a specific course from an event",
    response_description="Confirmation of course removal from the event",
)
def remove_course_from_event(event_id: int, course_id: int) -> None:
    """Removes a specific course from an event.

    args:
        event_id: The ID of the event
        course_id: The ID of the course to remove
    """
    ...