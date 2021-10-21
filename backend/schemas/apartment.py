from enum import Enum

from pydantic import BaseModel


class Status(str, Enum):
    FOR_SALE = 'for sale'
    TRADING = 'trading'
    SOLD_OUT = 'sold out'


class ApartmentBase(BaseModel):
    floor: int
    number: int
    area: float
    rooms: int
    start_price: int


class ApartmentIn(ApartmentBase):
    classes: list[str]


class Apartment(ApartmentBase):
    balcony: bool
    finishing: bool
    status: Status = Status.FOR_SALE

    class Config:
        orm_mode = True
