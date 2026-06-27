# __author__ = Issa Masumbuko

from typing import Annotated

from fastapi import APIRouter, Body

from ..models import (
    ActivateDormRoomsRequest,
    EventDormRoomResponse,
   
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
def activate_dorm_for_event(event_id: int, body: Annotated[ActivateDormRoomsRequest, Body()]) -> list[EventDormRoomResponse]:
    """Activates one or more dorm rooms for a specific event, making them available for participant assignments.

    args:
        event_id: The ID of the event for which dorm rooms are being activated.
        body: A JSON payload containing a list of dorm room IDs to activate for the event.
    
    returns:
        A list of the dorm rooms that were activated for the event, including their details and current
    """
    ...

@router.delete("/{room_id}",    
    summary="Deactivate a dorm for an event",
    response_description="Deactivates a specific dorm from being used for the event",
)
def deactivate_dorm_for_event(event_id: int, room_id: int) -> None:
    """Deactivates a specific dorm room from being used for a specific event.

    args:
        event_id: The ID of the event for which a dorm room is being deactivated.
        room_id: The ID of the dorm room to deactivate for the event.
    """
    ...

@router.get("/",
    summary="Get a list of all dorms activated for an event",
    response_description="Returns a list of all dorms activated for a specific event",
)
def list_dorms_for_event(event_id: int) -> list[EventDormRoomResponse]:
    """Returns a list of all dorm rooms that have been activated for a specific event.

    args:
        event_id: The ID of the event for which to list activated dorm rooms.
    
    returns:
        A list of all dorm rooms that are currently activated for the event, including their details and current assignment counts.
    """
    ...

@router.get("/{room_id}",
    summary="Get details of a specific dorm activated for an event",
    response_description="Returns the details of a specific dorm activated for a specific event",
)
def get_dorm_for_event(event_id: int, room_id: int) -> EventDormRoomResponse:
    """Returns the details of a specific dorm room that has been activated for a specific event.

    args:
        event_id: The ID of the event for which to get the dorm room details.
        room_id: The ID of the dorm room for which to get the details.          

    returns:
        The details of the specified dorm room
    """
    ...

