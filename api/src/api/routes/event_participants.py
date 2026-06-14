# __author__ = Issa Masumbuko
from fastapi import APIRouter
from coordinatetbi.tables.event import (
    EventParticipant,   
)

# from ..models import 

router = APIRouter(
    prefix="/event{event_id}/participants",
    tags=["Event Participants"],
)

# ---- Event Participants CRUD ----

@router.post("/",
    summary="Add a participant to an event",
    response_description="The details of the added participant",
)
def add_participant_to_event(event_id: int):
    ...

@router.put("/{participant_id}",
    summary="Update a specific participant in an event",
    response_description="The updated details of a specific participant in an event",
)
def update_event_participant(event_id: int, participant_id: int):
    ...

@router.get("/",
    summary="Get a list of all participants in an event",
    response_description="Returns a list of all participants in a specific event",
)
def list_event_participants(event_id: int):
    ... 

@router.get("/{participant_id}",
    summary="Get a specific participant in an event",
    response_description="Returns the details of a specific participant in an event",
)
def get_event_participant(event_id: int, participant_id: int):
    ...

@router.delete("/{participant_id}",
    summary="Remove a specific participant from an event",
    response_description="Removes a specific participant from an event",
)
def remove_event_participant(event_id: int, participant_id: int):
    ...
