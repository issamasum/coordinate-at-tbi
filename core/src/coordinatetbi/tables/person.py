# __author__ = Issa Masumbuko

"""Database-backed people models"""

import enum
from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, Text
from sqlmodel import (
    Field, 
    SQLModel,
    func,
    Enum,
)
class CoordinatorRole(str, enum.Enum):
    """Coordinating role a person can hold."""
    MAIN_COORDINATOR = "main coordinator"
    ASSISTANT_COORDINATOR = "assistant coordinator"

class Gender(str, enum.Enum):
    """Represents a person's gender."""
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"


class People(SQLModel, table=True):
    """Represents a person involved with the Triangle Baha'i Institute activities."""
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
    gender:Gender = Field(
        sa_column=Column(
            Enum(Gender, values_callable=lambda e: [m.value for m in e]),
            nullable=True
        )    
    )
    coordinator_role: CoordinatorRole = Field(
        sa_column=Column(
            Enum(CoordinatorRole, values_callable=lambda e: [m.value for m in e]),
            nullable=True
        )
    )
    data_of_birth: datetime = Field(
        sa_column=Column(
            DateTime(timezone=False),
            server_default=None,
            nullable=True
        ),
        default=None,
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