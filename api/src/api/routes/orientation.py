# __author__ = Issa Masumbuko

from typing import Annotated

from fastapi import APIRouter, Body

from ..models import (
    GenerateOrientationGroupsRequest,
    OrientationGroupAssignmentRequest,
    UpdateOrientationGroupRequest,
    OrientationGroupResponse,
    OrientationGroupSummary,
    OrientationParticipantResponse,
)

router = APIRouter(
    prefix="/events/{event_id}/orientation",
    tags=["Orientation Groups"],
)

# ---- Orientation Groups CRUD ----

@router.post("/",
    summary="Manually create a new orientation group in an event",
    response_description="The created orientation group details",
)
def create_orientation_group(
    event_id: int,
    body: Annotated[GenerateOrientationGroupsRequest, Body()],
) -> OrientationGroupResponse:
    """Manually creates a new orientation group in an event.

    args:
        event_id: The ID of the event to create an orientation group in
        body: Size constraints and minimum facilitator count for the group

    returns:
        The details of the created orientation group
    """
    ...


@router.post("/generate",
    summary="Automatically generate orientation groups for an event",
    response_description="The generated orientation groups",
)
def generate_orientation_groups(event_id: int) -> list[OrientationGroupResponse]:
    """Automatically generates orientation groups for an event based on
    its participants and facilitators.

    args:
        event_id: The ID of the event to generate orientation groups for

    returns:
        The generated orientation groups with their assigned participants and facilitators
    """
    ...


@router.get("/",
    summary="Get a list of all orientation groups in an event",
    response_description="Returns a list of all orientation groups in a specific event",
)
def list_orientation_groups(event_id: int) -> list[OrientationGroupSummary]:
    """Returns a list of all orientation groups in a specific event.

    args:
        event_id: The ID of the event to list orientation groups for

    returns:
        A list of all orientation groups in the event
    """
    ...


@router.get("/{group_id}",
    summary="Get a specific orientation group",
    response_description="Returns the details of a specific orientation group",
)
def get_orientation_group(event_id: int, group_id: int) -> OrientationGroupResponse:
    """Returns the details of a specific orientation group.

    args:
        event_id: The ID of the event the group belongs to
        group_id: The ID of the orientation group to retrieve

    returns:
        The details of the orientation group, including its participants and facilitators
    """
    ...


@router.patch("/{group_id}",
    summary="Update a specific orientation group",
    response_description="The updated details of a specific orientation group",
)
def update_orientation_group(
    event_id: int,
    group_id: int,
    body: Annotated[UpdateOrientationGroupRequest, Body()],
) -> OrientationGroupResponse:
    """Updates the name or status of a specific orientation group.

    args:
        event_id: The ID of the event the group belongs to
        group_id: The ID of the orientation group to update
        body: The new name and/or status for the group

    returns:
        The updated orientation group
    """
    ...


@router.delete("/{group_id}",
    summary="Delete a specific orientation group",
    response_description="Confirmation of orientation group deletion",
)
def delete_orientation_group(event_id: int, group_id: int) -> None:
    """Deletes a specific orientation group from the database.

    args:
        event_id: The ID of the event the group belongs to
        group_id: The ID of the orientation group to delete
    """
    ...


# ---- Orientation Participants CRUD ----

@router.post("/{group_id}/participants",
    summary="Add a participant to an orientation group",
    response_description="The added orientation participant details",
)
def add_participant_to_orientation_group(
    event_id: int,
    group_id: int,
    body: Annotated[OrientationGroupAssignmentRequest, Body()],
) -> OrientationParticipantResponse:
    """Adds a participant to a specific orientation group.

    args:
        event_id: The ID of the event the group belongs to
        group_id: The ID of the orientation group to add the participant to
        body: The participant ID and their role in the group

    returns:
        The details of the added orientation participant
    """
    ...


@router.get("/{group_id}/participants",
    summary="Get a list of all participants in an orientation group",
    response_description="Returns a list of all participants in a specific orientation group",
)
def list_participants_in_orientation_group(
    event_id: int,
    group_id: int,
) -> list[OrientationParticipantResponse]:
    """Returns a list of all participants in a specific orientation group.

    args:
        event_id: The ID of the event the group belongs to
        group_id: The ID of the orientation group to list participants for

    returns:
        A list of all participants in the orientation group
    """
    ...


@router.get("/participants/{participant_id}",
    summary="Get a specific orientation participant",
    response_description="Returns the details of a specific orientation participant",
)
def get_orientation_participant(
    event_id: int,
    participant_id: int,
) -> OrientationParticipantResponse:
    """Returns the details of a specific orientation participant.

    args:
        event_id: The ID of the event the participant belongs to
        participant_id: The ID of the orientation participant to retrieve

    returns:
        The details of the orientation participant, including their group and role
    """
    ...


@router.patch("/participants/{participant_id}",
    summary="Update a specific orientation participant",
    response_description="The updated details of a specific orientation participant",
)
def update_orientation_participant(
    event_id: int,
    participant_id: int,
    body: Annotated[OrientationGroupAssignmentRequest, Body()],
) -> OrientationParticipantResponse:
    """Updates the group assignment or role of a specific orientation participant.

    args:
        event_id: The ID of the event the participant belongs to
        participant_id: The ID of the orientation participant to update
        body: The updated group ID and/or role for the participant

    returns:
        The updated orientation participant
    """
    ...


@router.delete("/participants/{participant_id}",
    summary="Remove a participant from an orientation group",
    response_description="Confirmation of participant removal",
)
def remove_participant_from_orientation_group(event_id: int, participant_id: int) -> None:
    """Removes a specific participant from their orientation group.

    args:
        event_id: The ID of the event the participant belongs to
        participant_id: The ID of the orientation participant to remove
    """
    ...