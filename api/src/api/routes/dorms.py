# __author__ = Issa Masumbuko

from fastapi import APIRouter
from coordinatetbi.tables.dorm import (
    Dorm,
)

router = APIRouter(
    prefix="/cottages/{cottage_id}/dorms",
    tags=["Dorms"],
)

# ---- Dorms CRUD ----

@router.post("/",
    summary="Create a new dorm",
    response_description="The created dorm details",
)
def add_dorm_to_cottage(cottage_id: int):
    ...

@router.patch("/{dorm_id}",
    summary="Update a specific dorm",
    response_description="The updated details of a specific dorm",
)
def update_dorm(dorm_id: int):
    ... 

@router.get("/",
    summary="Get a list of all dorms in a cottage", 
    response_description="Returns a list of all dorms in a specific cottage",
)
def list_dorms_in_cottage(cottage_id: int):
    ...

@router.get("/{dorm_id}",
    summary="Get a specific dorm",
    response_description="Returns the details of a specific dorm",
)
def get_dorm(dorm_id: int):
    ... 

@router.delete("/{dorm_id}",
    summary="Delete a specific dorm",
    response_description="Deletes a specific dorm from the database",
)
def delete_dorm(dorm_id: int):
    ... 
