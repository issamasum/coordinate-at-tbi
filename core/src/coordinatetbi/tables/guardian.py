# __author__ = Issa Masumbuko

"""Database-backed guardian models"""

import enum

from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, Text
from sqlmodel import (
    Field, 
    SQLModel,
    func,
    Enum,
)
class Relationship(str, enum.Enum):
    """Enumerate the relationship a guardian can have with a person."""
    PARENT = "Parent"
    GUARDIAN = "Guardian"
    SIBLING = "Sibling"
    OTHER = "Other"

class Guardian(SQLModel, table=True):
    """Represents a guardian of a person involved with the Triangle Baha'i Institute activities."""
   
    id: int = Field(
        sa_column=Column(Integer, primary_key=True, autoincrement=True)
    )   
    name: str = Field(
        sa_column=Column(Text, nullable=False)
    )
    email: str = Field(
        sa_column=Column(Text, nullable=True)
    )
    phone: int = Field(
        sa_column=Column(Integer, nullable=True)
    )
    address: str = Field(
        sa_column=Column(Text, nullable=True)
    )
    deleted_at: datetime = Field(
        sa_column=Column(
            DateTime(timezone=True),
            server_default=func.now(),
            onupdate=func.now(),
            nullable=False,
        ),
        default=None,
    )

class PersonGuardian(SQLModel, table=True):
    """Represents the relationship between a person and their guardian."""

    __tablename__ = "personguardian"
    
    person_id: int = Field(
        sa_column=Column(Integer, ForeignKey("person.id"), primary_key=True)
    )
    guardian_id: int = Field(
        sa_column=Column(Integer, ForeignKey("guardian.id"), primary_key=True)
    )
    relationship: Relationship = Field(
        sa_column=Column(
            Enum(Relationship, values_callable=lambda e: [m.value for m in e]),
            nullable=False
        )
    )