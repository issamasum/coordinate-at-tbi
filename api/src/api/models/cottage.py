
# __author__ = Issa Masumbuko
 
"""Pydantic models for cottage and dorm endpoints."""
 
from typing import Optional
from pydantic import BaseModel
 
from tables.cottage import CottageGender
 
 
# ---- Cottage Models ----
 
class CreateCottageRequest(BaseModel):
    """Payload for creating a new cottage."""
    name: str
    gender: CottageGender
    is_active: bool = True
 
 
class UpdateCottageRequest(BaseModel):
    """Payload for updating an existing cottage."""
    name: Optional[str] = None
    gender: Optional[CottageGender] = None
    is_active: Optional[bool] = None
 
 
class CottageResponse(BaseModel):
    """A single cottage record returned from the API."""
    id: int
    name: str
    gender: CottageGender
    is_active: bool