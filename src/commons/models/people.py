from typing import Optional
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select
from sqlalchemy import UniqueConstraint


class PeopleBase(SQLModel):
    given_name: str = Field(max_length=48)
    family_name: str = Field(max_length=96)
    date_of_birth: str = Field(max_length=32)
    place_of_birth: Optional[str] = Field(max_length=96)


class People(PeopleBase, table=True):
    __table_args__ = (UniqueConstraint("given_name", "family_name", "date_of_birth", "place_of_birth"),)
    id: Optional[int] = Field(default=None, primary_key=True)
    given_name: str = Field(max_length=48)
    family_name: str = Field(max_length=96)
    date_of_birth: str = Field(max_length=32)
    place_id: Optional[int] = Field(default=None, foreign_key="places.id")
    place: Optional["Place"] = Relationship(back_populates="people")