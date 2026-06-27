 # __author__ = Issa Masumbuko

from typing import Annotated

from fastapi import APIRouter, Body

from ..models import (
    DormAssignmentRequest,
    GenerateDormAssignmentsRequest,
    UpdateDormAssignmentRequest,
    DormAssignmentResponse,
)

router = APIRouter(
    prefix="/events/{event_id}/dorm-assignments",
    tags=["Dorm Assignments"],
)

# ---- Dorm Assignments CRUD ----

@router.get("/",
    summary="Get a list of all dorm assignments for an event",
    response_description="Returns a list of all dorm assignments for a specific event",
)
def list_dorm_assignments_for_event(event_id: int) -> list[DormAssignmentResponse]:
    """Returns a list of all dorm assignments for a specific event.

    args:
        event_id: The ID of the event for which to list dorm assignments

    returns:
        A list of all dorm assignments for the event
    """
    ...


@router.get("/{assignment_id}",
    summary="Get a specific dorm assignment",
    response_description="Returns the details of a specific dorm assignment",
)
def get_dorm_assignment(event_id: int, assignment_id: int) -> DormAssignmentResponse:
    """Returns the details of a specific dorm assignment.

    args:
        event_id: The ID of the event the assignment belongs to
        assignment_id: The ID of the dorm assignment to retrieve

    returns:
        The details of the specified dorm assignment
    """
    ...


@router.post("/",
    summary="Manually assign a participant to a dorm room",
    response_description="The created dorm assignment details",
)
def manual_dorm_assignment(
    event_id: int,
    body: Annotated[DormAssignmentRequest, Body()],
) -> DormAssignmentResponse:
    """Manually assigns a single participant to a dorm room for a specific event.

    args:
        event_id: The ID of the event for which the assignment is being created
        body: The participant ID and the dorm room ID to assign them to

    returns:
        The created dorm assignment
    """
    ...


@router.post("/generate",
    summary="Automatically generate dorm assignments for an event",
    response_description="The generated dorm assignment details",
)
def generate_dorm_assignments(
    event_id: int,
    body: Annotated[GenerateDormAssignmentsRequest, Body()],
) -> list[DormAssignmentResponse]:
    """Triggers the automatic dorm-assignment algorithm for a specific event.

    args:
        event_id: The ID of the event for which to generate dorm assignments
        body: Options for the assignment algorithm

    returns:
        A list of the generated dorm assignments
    """
    ...


@router.patch("/{assignment_id}",
    summary="Update a specific dorm assignment",
    response_description="The updated details of a specific dorm assignment",
)
def update_dorm_assignment(
    event_id: int,
    assignment_id: int,
    body: Annotated[UpdateDormAssignmentRequest, Body()],
) -> DormAssignmentResponse:
    """Updates a specific dorm assignment's room or status.

    args:
        event_id: The ID of the event the assignment belongs to
        assignment_id: The ID of the dorm assignment to update
        body: The updated room or status for the assignment

    returns:
        The updated dorm assignment
    """
    ...


@router.delete("/{assignment_id}",
    summary="Delete a specific dorm assignment",
    response_description="Confirmation of dorm assignment deletion",
)
def delete_dorm_assignment(event_id: int, assignment_id: int) -> None:
    """Deletes a specific dorm assignment from the database.

    args:
        event_id: The ID of the event the assignment belongs to
        assignment_id: The ID of the dorm assignment to delete
    """
    ...