# __author__ = Issa Masumbuko

from typing import Annotated

from fastapi import APIRouter, Body

from ..models import (
    CreateGuardianRequest,
    UpdateGuardianRequest,
    GuardianResponse,
)

router = APIRouter(
    prefix="/guardians",
    tags=["Guardians"],
)

# ---- Guardians CRUD ----

@router.post("/",
    summary="Create a new guardian",
    response_description="The created guardian details",
)
def create_guardian(body: Annotated[CreateGuardianRequest, Body()]) -> GuardianResponse:
    """Creates a new guardian with the given details.

    args:
        body: The details of the guardian to create

    returns:
        The details of the created guardian
    """
    ...


@router.get("/",
    summary="Get a list of all guardians",
    response_description="Returns a list of all guardians in the database",
)
def list_guardians() -> list[GuardianResponse]:
    """Returns a list of all guardians in the database."""
    ...


@router.get("/{guardian_id}",
    summary="Get a specific guardian",
    response_description="Returns the details of a specific guardian",
)
def get_guardian(guardian_id: int) -> GuardianResponse:
    """Returns the details of a specific guardian.

    args:
        guardian_id: The ID of the guardian to retrieve

    returns:
        The details of the requested guardian
    """
    ...


@router.patch("/{guardian_id}",
    summary="Update a specific guardian",
    response_description="The updated details of a specific guardian",
)
def update_guardian(
    guardian_id: int,
    body: Annotated[UpdateGuardianRequest, Body()],
) -> GuardianResponse:
    """Updates the details of a specific guardian.

    args:
        guardian_id: The ID of the guardian to update
        body: The fields to update on the guardian

    returns:
        The updated details of the guardian
    """
    ...


@router.delete("/{guardian_id}",
    summary="Delete a specific guardian",
    response_description="Confirmation of guardian deletion",
)
def delete_guardian(guardian_id: int) -> None:
    """Deletes a specific guardian from the database.

    args:
        guardian_id: The ID of the guardian to delete
    """
    ...