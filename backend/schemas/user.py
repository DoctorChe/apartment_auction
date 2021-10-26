from pydantic import BaseModel, Field


class UserBase(BaseModel):
    name: str


class User(UserBase):
    id: int = Field(..., gt=0)

    class Config:
        orm_mode = True
