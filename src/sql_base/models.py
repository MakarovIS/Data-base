from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class Workers(BaseModel):
    id: int
    surname: str
    name: str
    date_of_birth: str
    experience: Optional[str]

class Spectacles(BaseModel):
    id: int
    name: str
    genre: str
    length: int

class Speechs(BaseModel):
    id: int
    spectacle_id: int
    hall: str
    date_and_time: datetime

class Employment_of_actors(BaseModel):
    id: int
    worker_id: int
    spectacle_id: int
    role_actor: str

class Ticket_price_categories(BaseModel):
    id: int
    hall: str
    row: str
    price: int

class Tickets(BaseModel):
    id: int
    ticket_price_category_id: int
    speech_id: int
    status: bool