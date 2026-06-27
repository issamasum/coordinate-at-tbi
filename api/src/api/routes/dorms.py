# __author__ = Issa Masumbuko

from typing import Annotated

from fastapi import APIRouter, Body

from ..models import (
    CreateDormRequest,
    UpdateDormRequest,
    DormResponse,
)

router = APIRouter(
    prefix="/cottages/{cottage_id}/dorms",
    tags=["Dorms"],
)

# ---- Dorms CRUD ----

@router.post("/",
    summary="Add a dorm room to a cottage",
    response_description="The created dorm room details",
)
def add_dorm_to_cottage(
    cottage_id: int,
    body: Annotated[CreateDormRequest, Body()],
) -> DormResponse:
    """Creates a new dorm room inside a specific cottage.

    args:
        cottage_id: The ID of the cottage to add the dorm room to
        body: The details of the dorm room to create

    returns:
        The created dorm room
    """
    ...


@router.get("/",
    summary="Get a list of all dorms in a cottage",
    response_description="Returns a list of all dorm rooms in a specific cottage",
)
def list_dorms_in_cottage(cottage_id: int) -> list[DormResponse]:
    """Returns all dorm rooms belonging to a specific cottage.

    args:
        cottage_id: The ID of the cottage to list dorm rooms for

    returns:
        A list of all dorm rooms in the cottage
    """
    ...


@router.get("/{dorm_id}",
    summary="Get a specific dorm room",
    response_description="Returns the details of a specific dorm room",
)
def get_dorm(cottage_id: int, dorm_id: int) -> DormResponse:
    """Returns the details of a specific dorm room.

    args:
        cottage_id: The ID of the cottage the dorm room belongs to
        dorm_id: The ID of the dorm room to retrieve

    returns:
        The details of the requested dorm room
    """
    ...


@router.patch("/{dorm_id}",
    summary="Update a specific dorm room",
    response_description="The updated details of a specific dorm room",
)
def update_dorm(
    cottage_id: int,
    dorm_id: int,
    body: Annotated[UpdateDormRequest, Body()],
) -> DormResponse:
    """Updates the details of a specific dorm room.

    args:
        cottage_id: The ID of the cottage the dorm room belongs to
        dorm_id: The ID of the dorm room to update
        body: The fields to update on the dorm room

    returns:
        The updated dorm room
    """
    ...


@router.delete("/{dorm_id}",
    summary="Delete a specific dorm room",
    response_description="Confirmation of dorm room deletion",
)
def delete_dorm(cottage_id: int, dorm_id: int) -> None:
    """Deletes a specific dorm room from a cottage.

    args:
        cottage_id: The ID of the cottage the dorm room belongs to
        dorm_id: The ID of the dorm room to delete
    """
    ...