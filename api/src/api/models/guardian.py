# __author__ = Issa Masumbuko

"""Pydantic models for guardian-related endpoints."""

from typing import Optional
from pydantic import BaseModel

from tables.guardian import GuardianRelationship


class CreateGuardianRequest(BaseModel):
    """Payload for adding a new guardian into the database."""
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None


class UpdateGuardianRequest(BaseModel):
    """Payload for updating an existing guardian's information."""
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None


class LinkGuardianRequest(BaseModel):
    """Payload for linking an existing guardian to a person."""
    guardian_id: int
    relationship: GuardianRelationship


class GuardianResponse(BaseModel):
    """Full guardian record returned from the API."""
    id: int
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None