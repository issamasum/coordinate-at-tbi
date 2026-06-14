# __author__ = Issa Masumbuko

"""Database-backed for all orientation models"""

import enum

from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlmodel import (
    Field, 
    SQLModel,
    Enum,
)

class OrientationGroupStatus(str, enum.Enum):
    """Enumeration for orientation group status."""
    DRAFT = "draft"
    CONFIRMED = "confirmed"
    CANCEL = "canceled"

class OrientationParticipantRole(str, enum.Enum):
    """Enumeration for orientation participant role."""
    FACILITATOR = "facilitator"
    PARTICIPANT = "participant"


class OrientationGroup(SQLModel, table=True):
    """Represents an orientation group at an event organized by the Triangle Baha'i Institute."""

    __tablename__ = "orientationgroup"

    id: int = Field(
        sa_column=Column(Integer, primary_key=True, autoincrement=True)
    )
    name: str = Field(
            sa_column=Column(Text, nullable=True)
    )
    event_id: int = Field(
        sa_column=Column(Integer, ForeignKey("event.id"), nullable=False)
    )
    status: OrientationGroupStatus = Field(
        sa_column=Column(
            Enum(OrientationGroupStatus, values_callable=lambda e: [m.value for m in e]),
            nullable=False
        )
    )


class OrientationParticipant(SQLModel, table=True):
    """Represents a participant in an orientation group at an event organized by the Triangle Baha'i Institute."""

    __tablename__ = "orientationparticipant"

    id: int = Field(
        sa_column=Column(Integer, primary_key=True, autoincrement=True)
    )
    name: str = Field(
            sa_column=Column(Text, nullable=False)
    )
    group_id: int = Field(
        sa_column=Column(Integer, ForeignKey("orientationgroup.id"), nullable=False)
    )
    partipant_id: int = Field(
        sa_column=Column(Integer, ForeignKey("eventparticipant.id"), nullable=False)
    )
    role: OrientationParticipantRole = Field(
        sa_column=Column(
            Enum(OrientationParticipantRole, values_callable=lambda e: [m.value for m in e]),
            nullable=False
        )
    )
