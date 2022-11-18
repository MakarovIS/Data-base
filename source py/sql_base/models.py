from typing import Optional
from pydantic import BaseModel


class Hall(BaseModel):
    id: Optional[int]
    name: str


class Actor(BaseModel):
    id: Optional[int]
    name_and_surname: str
    date_of_birth: str
    experience: int


class Genre(BaseModel):
    id: Optional[int]
    name: str


class Spectacle(BaseModel):
    id: Optional[int]
    name: str
    genre_id: int
    length: int


class Employment_of_actors(BaseModel):
    id: Optional[int]
    actor_id: int
    spectacle_id: int
    role: str


class Speech(BaseModel):
    id: Optional[int]
    spectacle_id: int
    hall_id: int
    date: str
    time: str


class Category(BaseModel):
    id: Optional[int]
    hall_id: int
    row: int
    price: int


class Ticket(BaseModel):
    id: Optional[int]
    category_id: int
    speech_id: int
    status: bool
