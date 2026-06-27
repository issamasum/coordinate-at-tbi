# __author__ = Issa Masumbuko

from typing import Annotated

from fastapi import APIRouter, Body

from ..models import (
    LinkGuardianRequest,
    GuardianResponse,
)

router = APIRouter(
    prefix="/people/{person_id}/guardians",
    tags=["People's Guardians"],
)

# ---- People Guardians CRUD ----

@router.post("/",
    summary="Link a guardian to a person",
    response_description="The details of the linked guardian",
)
def link_guardian_to_person(
    person_id: int,
    body: Annotated[LinkGuardianRequest, Body()],
) -> GuardianResponse:
    """Links an existing guardian to a person with a specified relationship.

    args:
        person_id: The ID of the person to link the guardian to
        body: The guardian ID and the relationship label

    returns:
        The details of the linked guardian
    """
    ...


@router.get("/",
    summary="Get a list of all guardians linked to a person",
    response_description="Returns a list of all guardians linked to a specific person",
)
def list_guardians_of_person(person_id: int) -> list[GuardianResponse]:
    """Returns all guardians linked to a specific person.

    args:
        person_id: The ID of the person to list guardians for

    returns:
        A list of all guardians linked to the person
    """
    ...


@router.delete("/{guardian_id}",
    summary="Unlink a guardian from a person",
    response_description="Confirmation of guardian unlinking",
)
def unlink_guardian_from_person(person_id: int, guardian_id: int) -> None:
    """Removes the link between a specific guardian and a person.

    args:
        person_id: The ID of the person
        guardian_id: The ID of the guardian to unlink
    """
    ...