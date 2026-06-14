# __author__ = Issa Masumbuko

from fastapi import APIRouter
from coordinatetbi.tables.dorm import (
    DormAssignment,
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
def list_dorm_assignments_for_event(event_id: int):
    ...

@router.get("/{assignment_id}", 
    summary="Get a specific dorm assignment",
    response_description="Returns the details of a specific dorm assignment",
)
def get_dorm_assignment(assignment_id: int):
    ...
# might not be needed
@router.get("/{assignment_id}/occupants",
    summary="Get the occupants of a specific dorm assignment",
    response_description="Returns a list of occupants assigned to a specific dorm assignment",
)
def get_dorm_assignment_occupants(assignment_id: int):
    ... 

@router.delete("/{assignment_id}",
    summary="Delete a specific dorm assignment",
    response_description="Deletes a specific dorm assignment from the database",
)
def delete_dorm_assignment(assignment_id: int):
    ...

@router.post("/",
    summary="Manually create a new dorm assignment for an event",
    response_description="The created dorm assignment details",
)
def manual_dorm_assignment(event_id: int):
    ...

@router.post("/generate",   
    summary="Automatically generate dorm assignments for an event",
    response_description="The generated dorm assignment details",
)
def generate_dorm_assignments(event_id: int):
    ...

@router.patch("/{assignment_id}",
    summary="Update a specific dorm assignment",
    response_description="The updated details of a specific dorm assignment",
)
def update_dorm_assignment(assignment_id: int):
    ...
    