# __author__ = Issa Masumbuko

from typing import Annotated

from fastapi import APIRouter, Body

from ..models import (
    CreateCottageRequest,
    UpdateCottageRequest,
    CottageResponse,
)

router = APIRouter(
    prefix="/cottages",
    tags=["Cottages"],
)

# ---- Cottage CRUD ----

@router.post("/",
    summary="Create a new cottage",
    response_description="The created cottage",
)
def create_cottage(body: Annotated[CreateCottageRequest, Body()]) -> CottageResponse:
    """Creates a new cottage.

    args:
        body: The details of the cottage to create

    returns:
        The created cottage
    """
    ...


@router.get("/",
    summary="Get all cottages",
    response_description="List of all cottages",
)
def list_cottages() -> list[CottageResponse]:
    """Returns a list of all cottages."""
    ...


@router.get("/{cottage_id}",
    summary="Get a specific cottage",
    response_description="The requested cottage details",
)
def get_cottage(cottage_id: int) -> CottageResponse:
    """Returns the details of a specific cottage.

    args:
        cottage_id: The ID of the cottage to retrieve

    returns:
        The requested cottage
    """
    ...


@router.patch("/{cottage_id}",
    summary="Update a specific cottage",
    response_description="The updated cottage details",
)
def update_cottage(
    cottage_id: int,
    body: Annotated[UpdateCottageRequest, Body()],
) -> CottageResponse:
    """Updates the details of a specific cottage.

    args:
        cottage_id: The ID of the cottage to update
        body: The fields to update on the cottage

    returns:
        The updated cottage
    """
    ...


@router.delete("/{cottage_id}",
    summary="Delete a specific cottage",
    response_description="Confirmation of cottage deletion",
)
def delete_cottage(cottage_id: int) -> None:
    """Deletes a specific cottage.

    args:
        cottage_id: The ID of the cottage to delete
    """
    ...