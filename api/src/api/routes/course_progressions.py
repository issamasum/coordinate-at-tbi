# __author__ = Issa Masumbuko

from typing import Annotated, Optional

from fastapi import APIRouter, Body, Query

from tables.course_progression import CourseProgressionStatus
from ..models import (
    CourseProgressionsRequest,
    CourseProgressionItem,
    CourseProgressionResponse,
)

router = APIRouter(
    prefix="/course_progressions",
    tags=["Course Progressions"],
)


@router.post("/",
    summary="Create or update course progressions for a person",
    response_description="The created or updated course progression records",
)
def upsert_course_progressions(
    body: Annotated[CourseProgressionsRequest, Body()],
) -> list[CourseProgressionResponse]:
    """Creates or updates one or more course progressions for a person.
    Pass a single item in progressions for a one-off update.

    args:
        body: The person ID and list of course + status pairs to upsert

    returns:
        The created or updated course progression records
    """
    ...


@router.get("/",
    summary="List course progressions",
    response_description=(
        "Returns all course progressions. "
        "Filter by person_id to see one person's courses, "
        "or by course_id to see everyone on a given course."
    ),
)
def list_course_progressions(
    person_id: Optional[int] = Query(None, description="Filter by person"),
    course_id: Optional[int] = Query(None, description="Filter by course"),
    status: Optional[CourseProgressionStatus] = Query(None, description="Filter by status"),
) -> list[CourseProgressionResponse]:
    """Returns course progressions, optionally filtered by person, course, or status."""
    ...


@router.get("/{progression_id}",
    summary="Get a specific course progression",
    response_description="Returns the details of a specific course progression",
)
def get_course_progression(progression_id: int) -> CourseProgressionResponse:
    """Returns the details of a specific course progression record.

    args:
        progression_id: The ID of the course progression to retrieve

    returns:
        The details of the requested course progression
    """
    ...


@router.patch("/{progression_id}",
    summary="Update a specific course progression",
    response_description="The updated course progression record",
)
def update_course_progression(
    progression_id: int,
    body: Annotated[CourseProgressionItem, Body()],
) -> CourseProgressionResponse:
    """Updates the course and/or status of a specific course progression.

    args:
        progression_id: The ID of the course progression to update
        body: The updated course ID and status

    returns:
        The updated course progression record
    """
    ...