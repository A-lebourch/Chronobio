from pydantic import BaseModel


class FieldGamedata(BaseModel):
    location: str
    bought: bool
    content: str
    needed_water: int
