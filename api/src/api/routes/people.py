# __author__ = Issa Masumbuko

from fastapi import APIRouter 
from coordinatetbi.tables import Person



router = APIRouter(
    prefix="/people",
    tags=["People"],
)

# ----- Person CRUD ----- 

@router.post("/",
    summary="Create a new person",
    response_description="The details of the created person", 
)
def create_person():
    pass

@router.patch("/{person_id}",
    summary="Update an existing person",
    response_description="The details of the updated person",
)
def update_person(person_id: int):
    pass    

@router.get("/",
    summary="Get a list of all people",
    response_description="A list of people",
)
def list_people():
    pass

@router.get("/{person_id}",
    summary="Get details of a specific person",
    response_description="The details of the specified person",
)
def get_person(person_id: int):
    pass
