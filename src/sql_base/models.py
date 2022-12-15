from typing import Optional
from pydantic import BaseModel


class Workers(BaseModel):
    id: Optional[int]
    surname: str
    name: str
    date_of_birth: str
    experience: int