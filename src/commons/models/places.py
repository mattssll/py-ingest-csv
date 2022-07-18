from typing import Optional
from sqlmodel import Field, Relationship, SQLModel
from sqlalchemy import UniqueConstraint
#pydantic

class PlacesBase(SQLModel):
    city: str = Field(max_length=96)
    county: str = Field(max_length=96)
    country: str = Field(max_length=48)


class Places(PlacesBase, table=True):
    __table_args__ = (UniqueConstraint("city", "county", "country"),)
    id: Optional[int] = Field(default=None, primary_key=True)
    #uuid
    people: Optional["People"] = Relationship(back_populates="place")
