# __author__ = Issa Masumbuko

from fastapi import APIRouter
from coordinatetbi.tables.guardian import (
    Guardian,
    PersonGuardian
)
  
router = APIRouter(
    prefix="/people/{person_id}guardians",
    tags=["People's Guardians"],
)

# ---- People Guardians CRUD ----

@router.post("/",
    summary="Link a guardian to a person",
    response_description="The details of the linked guardian",
)
def link_guardian_to_person(person_id: int):
    ... 

@router.get("/",
    summary="Get a list of all guardians linked to a person",
    response_description="Returns a list of all guardians linked to a specific person",
)
def list_guardians_of_person(person_id: int):
    ...

@router.delete("/{guardian_id}",
    summary="Unlink a guardian from a person",
    response_description="Unlinks a specific guardian from a specific person",
)
def delete_person_to_guardian_link(person_id: int, guardian_id: int):
    ...

