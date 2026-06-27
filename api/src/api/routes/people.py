# __author__ = Issa Masumbuko

from typing import Annotated, Optional

from fastapi import APIRouter, Body, Query

from tables.person import Gender, CoordinatorRole
from tables.course_progression import CourseProgressionStatus
from ..models import (
    CreatePersonRequest,
    UpdatePersonRequest,
    PersonResponse,
    PersonDetailResponse,
    CourseProgressionsRequest,
    CourseProgressionItem,
    CourseProgressionResponse,
)

router = APIRouter(
    prefix="/people",
    tags=["People"],
)

# ---- Person CRUD ----

@router.post("/",
    summary="Create a new person",
    response_description="The details of the created person",
)
def create_person(body: Annotated[CreatePersonRequest, Body()]) -> PersonResponse:
    """Creates a new person with the given details.

    args:
        body: The details of the person to create

    returns:
        The created person
    """
    ...


@router.get("/",
    summary="Get a list of all people",
    response_description="A list of people, optionally filtered",
)
def list_people(
    name: Optional[str] = Query(None, description="Filter by partial name match"),
    gender: Optional[Gender] = Query(None, description="Filter by gender"),
    coordinator_role: Optional[CoordinatorRole] = Query(None, description="Filter by coordinator role"),
) -> list[PersonResponse]:
    """Returns a list of all people, optionally filtered by name, gender, or coordinator role."""
    ...


@router.get("/{person_id}",
    summary="Get the full profile of a specific person",
    response_description="The full profile of the specified person",
)
def get_person(person_id: int) -> PersonDetailResponse:
    """Returns the full profile of a specific person, including guardians,
    course progressions, and event history.

    args:
        person_id: The ID of the person to retrieve

    returns:
        The full profile of the requested person
    """
    ...


@router.patch("/{person_id}",
    summary="Update an existing person",
    response_description="The details of the updated person",
)
def update_person(
    person_id: int,
    body: Annotated[UpdatePersonRequest, Body()],
) -> PersonResponse:
    """Updates an existing person with the given details.

    args:
        person_id: The ID of the person to update
        body: The fields to update on the person

    returns:
        The updated person
    """
    ...


@router.delete("/{person_id}",
    summary="Delete a specific person",
    response_description="Confirmation of person deletion",
)
def delete_person(person_id: int) -> None:
    """Soft-deletes a specific person (sets deleted_at timestamp).

    args:
        person_id: The ID of the person to delete
    """
    ...


# ---- Person course progressions ----

@router.post("/{person_id}/course_progressions",
    summary="Create or update course progressions for a person",
    response_description="The created or updated course progression records",
)
def add_person_course_progressions(
    person_id: int,
    body: Annotated[CourseProgressionsRequest, Body()],
) -> list[CourseProgressionResponse]:
    """Creates or updates one or more course progressions for a person.
    person_id in the body is ignored; the URL param takes precedence.

    args:
        person_id: The ID of the person
        body: The list of course + status pairs to upsert

    returns:
        The created or updated course progression records
    """
    ...


@router.get("/{person_id}/course_progressions",
    summary="List all course progressions for a person",
    response_description="All course progressions belonging to the specified person",
)
def list_person_course_progressions(
    person_id: int,
    status: Optional[CourseProgressionStatus] = Query(None, description="Filter by status"),
) -> list[CourseProgressionResponse]:
    """Returns all course progressions for a specific person, optionally filtered by status.

    args:
        person_id: The ID of the person
        status: Optional filter by progression status

    returns:
        A list of course progressions for the person
    """
    ...


@router.patch("/{person_id}/course_progressions/{progression_id}",
    summary="Update a specific course progression for a person",
    response_description="The updated course progression record",
)
def update_person_course_progression(
    person_id: int,
    progression_id: int,
    body: Annotated[CourseProgressionItem, Body()],
) -> CourseProgressionResponse:
    """Updates a specific course progression for a person.

    args:
        person_id: The ID of the person
        progression_id: The ID of the course progression to update
        body: The updated course ID and status

    returns:
        The updated course progression record
    """
    ...


@router.delete("/{person_id}/course_progressions/{progression_id}",
    summary="Delete a specific course progression for a person",
    response_description="Confirmation of course progression deletion",
)
def delete_person_course_progression(person_id: int, progression_id: int) -> None:
    """Deletes a specific course progression record for a person.

    args:
        person_id: The ID of the person
        progression_id: The ID of the course progression to delete
    """
    ...