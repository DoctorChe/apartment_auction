import datetime

from sqlalchemy.orm import Session

from backend import models, schemas, crud


def create_bid(db: Session, auction_id: int, apartment_id: int, amount: int) -> schemas.Bid:
    auction = crud.read_auction(db, auction_id)
    auction = crud.update_auction(db, auction=auction, time_last_bid=datetime.datetime.now(datetime.timezone.utc))
    apartment = crud.read_apartment(db, apartment_id)
    bid_db = models.Bid(auction_id=auction.id, apartment_id=apartment.id, amount=amount)
    db.add(bid_db)
    db.commit()
    db.refresh(bid_db)
    return bid_db
