# __author__ = Issa Masumbuko

"""Database-backed guardian models"""

import enum
from datetime import datetime
from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import Column, DateTime, ForeignKey, Integer, Text
from sqlmodel import Field, Relationship, SQLModel, func, Enum

if TYPE_CHECKING:
    from .person import Person


class GuardianRelationship(str, enum.Enum):
    PARENT = "Parent"
    GUARDIAN = "Guardian"
    SIBLING = "Sibling"
    OTHER = "Other"


class Guardian(SQLModel, table=True):
    """Represents a guardian of a person involved with the Triangle Baha'i Institute."""

    __tablename__ = "guardian"

    id: int = Field(
        sa_column=Column(
            Integer, 
            primary_key=True, 
            autoincrement=True
            )
    )
    name: str = Field(
        sa_column=Column(
            Text, 
            nullable=False
            )
    )
    email: Optional[str] = Field(
        default=None, 
        sa_column=Column(
            Text, 
            nullable=True
            )
    )
    phone: Optional[str] = Field(
        default=None, 
        sa_column=Column(
            Text, 
            nullable=True
            )
    )
    address: Optional[str] = Field(
        default=None, 
        sa_column=Column(
            Text, 
            nullable=True
            )
    )
    created_at: datetime = Field(
        sa_column=Column(
            DateTime(timezone=True), 
            server_default=func.now(), 
            nullable=False
            ),
        default=None,
    )
    deleted_at: Optional[datetime] = Field(
        default=None, 
        sa_column=Column(
            DateTime(timezone=True), 
            nullable=True
        )
    )
    people: List["Person"] = Relationship(
        back_populates="guardians",
        sa_relationship_kwargs={"secondary": "personguardian", "lazy": "select"},
    )


class PersonGuardian(SQLModel, table=True):
    """Association table linking a Person to a Guardian with a relationship label."""

    __tablename__ = "personguardian"

    person_id: int = Field(
        sa_column=Column(
            Integer, 
            ForeignKey("person.id"), 
            primary_key=True
        )
    )
    guardian_id: int = Field(
        sa_column=Column(
            Integer, 
            ForeignKey("guardian.id"), 
            primary_key=True
        )
    )
    relationship: GuardianRelationship = Field(
        sa_column=Column(
            Enum(GuardianRelationship, values_callable=lambda e: [m.value for m in e]),
            nullable=False,
        )
    )