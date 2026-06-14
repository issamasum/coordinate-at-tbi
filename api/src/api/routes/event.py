# __author__ = Issa Masumbuko

from fastapi import APIRouter
from coordinatetbi.tables.event import (
    Event,

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
def create_event():
    ...

@router.patch("/{event_id}",
    summary="Update a specific event",
    response_description="The updated details of a specific event",
)
def update_event(event_id: int):
    ...

@router.get("/",
    summary="Get a list of all events",
    response_description="Returns a list of all events in the database",
)
def list_events():
    ...

@router.get("/{event_id}",
    summary="Get a specific event",
    response_description="Returns the details of a specific event",
)
def get_event(event_id: int):
    ...
