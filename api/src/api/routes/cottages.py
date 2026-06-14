# __author__ = Issa Masumbuko

from fastapi import APIRouter, Depends

from coordinatetbi.tables import Cottage

# need to add cottage models

router = APIRouter(
    prefix="/cottages",
    tags=["Cottages"],
)

# --- Cottage CRUD ----

@router.post("/",
    summary="Create a new cottage",
    response_description="The created cottage",
)
def create_cottage():
    ...

@router.get("/",
    response_model=list[Cottage],
    summary="Get all cottages",
    response_description="List of all cottages",
)
def list_cottages():
    ...

@router.get("/{cottage_id}",
   summary="Get a specific cottage",
   response_description="The requested cottage details",
)
def get_cottage(cottage_id: int):
    ...

@router.patch("/{cottage_id}",
    summary="Update a specific cottage",
    response_description="The updated cottage details",
)
def update_cottage(cottage_id: int):
    ...

@router.delete("/{cottage_id}",
    summary="Delete a specific cottage",
    response_description="Confirmation of cottage deletion",
)
def delete_cottage(cottage_id: int):
    ...