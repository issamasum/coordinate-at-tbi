# __author__ = Issa Masumbuko

"""Database-backed cottage models"""
import enum


from sqlalchemy import Column, Integer, Text, UniqueConstraint
from sqlmodel import (
    Field, 
    SQLModel,
    Enum,
)

class CottageGender(str, enum.Enum):
    """Enumeration for cottage gender designations."""
    MALE = "Male"
    FEMALE = "Female"
    
class Cottage(SQLModel, table=True):
    """Represents a cottage used for overnight events organized by the Triangle Baha'i Institute."""
    __table_args__ = (
        UniqueConstraint("name", name="unique_cottage_name"),
    )
    
    id: int = Field(
        sa_column=Column(Integer, primary_key=True, autoincrement=True)
    )
    name: str = Field(
            sa_column=Column(Text, nullable=False)
    )
    gender: CottageGender = Field(
        sa_column=Column(
            Enum(CottageGender, values_callable=lambda e: [m.value for m in e]),
            nullable=False
        )
    )  
    is_available: bool = Field()