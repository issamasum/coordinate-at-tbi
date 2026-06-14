# __author__ = Issa Masumbuko

from fastapi import APIRouter
from coordinatetbi.tables import Guardian

router = APIRouter(
    prefix="/guardians",
    tags=["Guardians"],
)   

# ---- Guardians CRUD ----

@router.post("/",
    summary="Create a new guardian",
    response_description="The created guardian details",
)
def create_guardian():
    ...

@router.patch("/{guardian_id}",
    summary="Update a specific guardian",
    response_description="The updated details of a specific guardian",
)
def update_guardian(guardian_id: int):
    ...

@router.get("/",
    summary="Get a list of all guardians",
    response_description="Returns a list of all guardians in the database",
)
def list_guardians():
    ...

@router.get("/{guardian_id}",
    summary="Get a specific guardian",
    response_description="Returns the details of a specific guardian",
)
def get_guardian(guardian_id: int):
    ... 

@router.delete("/{guardian_id}",
    summary="Delete a specific guardian",
    response_description="Deletes a specific guardian from the database",
)
def delete_guardian(guardian_id: int):
    ...