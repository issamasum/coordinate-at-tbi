# __author__ = Issa Masumbuko

from fastapi import APIRouter
from coordinatetbi.tables.orientation import (
    OrientationGroup,
    OrientationParticipant,
)

router = APIRouter(
    prefix="/events/{event_id}/orientation",
    tags=["Orientation Groups"],   
)

# ---- Orientation Groups CRUD ----

@router.get("/",
    summary="Get a list of all orientation groups in an event",
    response_description="Returns a list of all orientation groups in a specific event",
)
def list_orientation_groups_in_event(event_id: int):
    ...

@router.get("/{group_id}",
    summary="Get a specific orientation group",
    response_description="Returns the details of a specific orientation group",
)
def get_orientation_group(group_id: int):
    ...

@router.delete("/{group_id}",
    summary="Delete a specific orientation group",
    response_description="Deletes a specific orientation group from the database",
)
def delete_orientation_group(group_id: int):
    ... 

@router.post("/",
    summary="Manually create a new orientation group in an event",
    response_description="The created orientation group details",
)
def create_orientation_group_in_event(event_id: int):
    ...

@router.post("/generate",
    summary="Automatically generate orientation groups for an event",
    response_description="The generated orientation groups details",
)   
def generate_orientation_groups_for_event(event_id: int):
    ... 

@router.patch("/{group_id}",
    summary="Update a specific orientation group",
    response_description="The updated details of a specific orientation group",
)
def update_orientation_group(group_id: int):
    ...


# ---- Orientation Participants CRUD ----

@router.post("/{group_id}/participants",
    summary="Add a participant to an orientation group",
    response_description="The added orientation participant details",
)
def add_participant_to_orientation_group(group_id: int):
    ...

@router.delete("/participants/{participant_id}",
    summary="Remove a participant from an orientation group",
    response_description="Removes a specific participant from an orientation group in the database",
)
def remove_participant_from_orientation_group(participant_id: int):
    ...

@router.patch("/participants/{participant_id}",
    summary="Update a specific orientation participant",
    response_description="The updated details of a specific orientation participant",
)
def update_orientation_participant(participant_id: int):
    ...

@router.get("/{group_id}/participants",
    summary="Get a list of all participants in an orientation group",
    response_description="Returns a list of all participants in a specific orientation group",
)
def list_participants_in_orientation_group(group_id: int):
    ...

@router.get("/participants/{participant_id}",
    summary="Get a specific orientation participant",
    response_description="Returns the details of a specific orientation participant",
)
def get_orientation_participant(participant_id: int):
    ...
