from datetime import datetime

from pydantic import BaseModel


class OrderCreate(BaseModel):
    id: int
    name_owner: str
    status: str
    price: int
    composition: str
    created_at: datetime
