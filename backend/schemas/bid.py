from datetime import datetime

from pydantic import BaseModel, Field


class BidBase(BaseModel):
    apartment_id: int = Field(..., gt=0)
    auction_id: int = Field(..., gt=0)
    amount: int = Field(..., gt=0)


class Bid(BidBase):
    id: int = Field(..., gt=0)
    timestamp: datetime

    class Config:
        orm_mode = True
