# __author__ = Issa Masumbuko

from typing import Annotated

from fastapi import APIRouter, Body

from ..models import (
    AddEventParticipantsRequest,
    UpdateEventParticipantRequest,
    EventParticipantResponse,
)

router = APIRouter(
    prefix="/events/{event_id}/participants",
    tags=["Event Participants"],
)

# ---- Event Participants CRUD ----

@router.post("/",
    summary="Add participants to an event",
    response_description="The details of the added participants",
)
def add_participants_to_event(
    event_id: int,
    body: Annotated[AddEventParticipantsRequest, Body()],
) -> list[EventParticipantResponse]:
    """Adds one or more participants to an event.

    args:
        event_id: The ID of the event to add participants to
        body: The IDs of the people to add as participants

    returns:
        The details of the added participants
    """
    ...


@router.get("/",
    summary="Get a list of all participants in an event",
    response_description="Returns a list of all participants in a specific event",
)
def list_event_participants(event_id: int) -> list[EventParticipantResponse]:
    """Returns a list of all participants in a specific event.

    args:
        event_id: The ID of the event to list participants for

    returns:
        A list of all participants in the event
    """
    ...


@router.get("/{participant_id}",
    summary="Get a specific participant in an event",
    response_description="Returns the details of a specific participant in an event",
)
def get_event_participant(event_id: int, participant_id: int) -> EventParticipantResponse:
    """Returns the details of a specific participant in an event.

    args:
        event_id: The ID of the event the participant is in
        participant_id: The ID of the participant to retrieve

    returns:
        The details of the requested participant
    """
    ...


@router.patch("/{participant_id}",
    summary="Update a specific participant in an event",
    response_description="The updated details of a specific participant in an event",
)
def update_event_participant(
    event_id: int,
    participant_id: int,
    body: Annotated[UpdateEventParticipantRequest, Body()],
) -> EventParticipantResponse:
    """Updates the roles, attendance, or overnight status of a specific participant.
    Only fields that are set will be updated.

    args:
        event_id: The ID of the event the participant is in
        participant_id: The ID of the participant to update
        body: The fields to update on the participant

    returns:
        The updated details of the participant
    """
    ...


@router.delete("/{participant_id}",
    summary="Remove a specific participant from an event",
    response_description="Confirmation of participant removal",
)
def remove_event_participant(event_id: int, participant_id: int) -> None:
    """Removes a specific participant from an event.

    args:
        event_id: The ID of the event the participant is in
        participant_id: The ID of the participant to remove
    """
    ...