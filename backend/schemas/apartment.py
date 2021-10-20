from pydantic import BaseModel


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

    class Config:
        orm_mode = True
