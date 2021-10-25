from datetime import datetime
from typing import Optional

from sqlalchemy import desc
from sqlalchemy.orm import Session

from backend import models, schemas
from backend.core.logger_config import get_logger

logger = get_logger(__name__)


def create_auction(db: Session, bid_duration: int) -> schemas.Auction:
    auction_db = models.Auction(bid_duration=bid_duration)
    db.add(auction_db)
    db.commit()
    db.refresh(auction_db)
    return auction_db


def read_auction(db: Session, auction_id: int) -> schemas.Auction:
    return db.query(models.Auction).filter(models.Auction.id == auction_id).first()


def update_auction(db: Session, auction: models.Auction,
                   time_last_bid: datetime):
    auction.time_last_bid = time_last_bid
    db.commit()
    return auction


def read_last_not_finished(db: Session) -> Optional[schemas.Auction]:
    return db.query(models.Auction).filter(models.Auction.finished.is_(False)). \
        order_by(desc(models.Auction.time_start)).first()
