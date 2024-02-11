from pydantic import BaseModel


class AddPosition(BaseModel):
    id: int
    actuality: bool = True
    price: int
    title: str

class UpdatePosition(BaseModel):
    id: int
    actuality: bool = True
    price: int
    title: str