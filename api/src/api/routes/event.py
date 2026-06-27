# __author__ = Issa Masumbuko

from typing import Annotated

from fastapi import APIRouter, Body

from ..models import (
    CreateEventRequest,
    UpdateEventRequest,
    EventResponse,
    EventDetailResponse,
)

router = APIRouter(
    prefix="/events",
    tags=["Events"],
)

# ---- Events CRUD ----

@router.post("/",
    summary="Create a new event",
    response_description="The created event details",
)
def create_event(body: Annotated[CreateEventRequest, Body()]) -> EventResponse:
    """Creates a new event with the given details.

    args:
        body: The details of the event to create

    returns:
        The created event
    """
    ...


@router.get("/",
    summary="Get a list of all events",
    response_description="Returns a list of all events in the database",
)
def list_events() -> list[EventResponse]:
    """Returns a list of all events in the database."""
    ...


@router.get("/{event_id}",
    summary="Get a specific event",
    response_description="Returns the details of a specific event",
)
def get_event(event_id: int) -> EventDetailResponse:
    """Returns the details of a specific event.

    args:
        event_id: The ID of the event to retrieve

    returns:
        The full details of the requested event
    """
    ...


@router.patch("/{event_id}",
    summary="Update a specific event",
    response_description="The updated details of a specific event",
)
def update_event(
    event_id: int,
    body: Annotated[UpdateEventRequest, Body()],
) -> EventResponse:
    """Updates the details of a specific event.

    args:
        event_id: The ID of the event to update
        body: The fields to update on the event

    returns:
        The updated event
    """
    ...