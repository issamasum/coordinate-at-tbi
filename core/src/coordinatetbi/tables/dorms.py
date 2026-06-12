# __author__ = Issa Masumbuko

"""Database-backed for all dorm facing models"""

import enum

from sqlalchemy import Column, Integer, Text, ForeignKey, UniqueConstraint
from sqlmodel import (
    Field, 
    SQLModel,
    Enum,
)

class DormAssignmentStatus(str, enum.Enum):
    """Enumeration for dorm assignment status."""
    ASSIGNED = "draft"
    UNASSIGNED = "confirmed"
    CANCELED = "canceled"

class Dorm(SQLModel, table=True):
    """Represents a dorm room at the Triangle Baha'i Institute Facility."""
   
    __table_args__ = (
        UniqueConstraint("name", name="unique_dorm_name"),
    )

    id: int = Field(
        sa_column=Column(Integer, primary_key=True, autoincrement=True)
    )
    name: str = Field(
            sa_column=Column(Text, nullable=False)
    )
    cottage_id: int = Field(
        sa_column=Column(Integer, ForeignKey("cottage.id"), nullable=False)
    )
    is_available: bool = Field()


class EventDormRoom(SQLModel, table=True):
    """Represents a dorm room used for an overnight event organized by the Triangle Baha'i Institute."""

    __tablename__ = "eventdormroom"
    __table_args__ = (
        UniqueConstraint("dorm_id", "event_id", name="unique_event_dorm_room"),
    ) 

    id: int = Field(
        sa_column=Column(Integer, primary_key=True, autoincrement=True)
    )
    dorm_id: int = Field(
        sa_column=Column(Integer, ForeignKey("dorm.id"), nullable=False)
    )
    event_id: int = Field(
        sa_column=Column(Integer, ForeignKey("event.id"), nullable=False)
    )


class DormAssignment(SQLModel, table=True):
    """Represents a dorm room assignment for an overnight event organized by the Triangle Baha'i Institute."""

    __tablename__ = "dormassignment"

    id: int = Field(
        sa_column=Column(Integer, primary_key=True, autoincrement=True)
    )
    event_dorm_id: int = Field(
        sa_column=Column(Integer, ForeignKey("eventdormroom.id"), nullable=False)
    )
    
    participant_id: int = Field(
        sa_column=Column(Integer, ForeignKey("eventparticipant.id"), nullable=False)
    )
    status: DormAssignmentStatus = Field(
        sa_column=Column(
            Enum(DormAssignmentStatus, values_callable=lambda e: [m.value for m in e]),
            nullable=False
        )
    )