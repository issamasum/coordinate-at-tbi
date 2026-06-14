# __author__ = Issa Masumbuko

from fastapi import APIRouter
from coordinatetbi.tables import BookProgression

# import models

router = APIRouter(
    prefix="/book_progressions",
    tags=["Book Progressions"],
) 

# ---- Book Progressions CRUD ----

@router.post("/",
        response_model=BookProgression,
        summary="Create a new book progression",
)
def create_book_progression():
    ... 

@router.get("/",
        response_model=list[BookProgression],
        summary="Get a list of all book progressions",
        response_description="Returns a list of all book progressions in the database",
)
def list_book_progressions():
    ... 
@router.get("/{book_progression_id}",
        response_model=BookProgression,
        summary="Get a specifc book progression",
        response_description="Returns a details of a specific book progression",
)
def get_book_progression(book_progression_id: int):
    ...
@router.patch("/{book_progression_id}",
        response_model=BookProgression,
        summary="Update a specific book progression",
        response_description="Returns the updated details of a specific book progression",
)
def update_book_progression(book_progression_id: int):
    ...