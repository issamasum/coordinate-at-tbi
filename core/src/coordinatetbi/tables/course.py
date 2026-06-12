# __author__ = Issa Masumbuko

"""Database-backed books models"""


from sqlalchemy import Column, Integer, Text
from sqlmodel import (
    Field, 
    SQLModel,
    UniqueConstraint,
)
class Course(SQLModel, table=True):
    """Represents Institute Courses offered by the Triangle Baha'i Institute."""

    __table_args__ = (
        UniqueConstraint("name", name="unique_course_name"),
        UniqueConstraint("title", name="unique_course_title"),
    )  

    id: int = Field(
        sa_column=Column(Integer, primary_key=True, autoincrement=True)
    )
    name: str = Field(
            sa_column=Column(Text, nullable=False)
    )
    title: str = Field(
            sa_column=Column(Text, nullable=False)
    )
