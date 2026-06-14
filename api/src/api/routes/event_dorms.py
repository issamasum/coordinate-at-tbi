# __author__ = Issa Masumbuko

from fastapi import APIRouter
from coordinatetbi.tables.dorm import (
    EventDormRoom,
)

router = APIRouter(
    prefix="/events/{event_id}/dorms",
    tags=["Event Dorms"],
)   

# ---- Event Dorms CRUD ----

@router.post("/",
    summary="Activate a dorm for an event",
    response_description="The details of the dorm activated for the event",
)
def activate_dorm_for_event(event_id: int):
    ...

@router.delete("/{room_id}",    
    summary="Deactivate a dorm for an event",
    response_description="Deactivates a specific dorm from being used for the event",
)
def deactivate_dorm_for_event(event_id: int, room_id: int):
    ...

@router.get("/",
    summary="Get a list of all dorms activated for an event",
    response_description="Returns a list of all dorms activated for a specific event",
)
def list_dorms_for_event(event_id: int):
    ...

@router.get("/{room_id}",
    summary="Get details of a specific dorm activated for an event",
    response_description="Returns the details of a specific dorm activated for a specific event",
)
def get_dorm_for_event(event_id: int, room_id: int):
    ...

