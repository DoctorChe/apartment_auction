from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class AuctionBase(BaseModel):
    id: int = Field(..., gt=0)
    bid_duration: int = Field(..., gt=0)


class Auction(AuctionBase):
    time_start: datetime
    time_last_bid: Optional[datetime]
    time_finish: datetime
    finished: bool

    class Config:
        orm_mode = True
