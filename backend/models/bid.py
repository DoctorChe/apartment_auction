from sqlalchemy import Column, Integer, Identity, DateTime, func, ForeignKey

from backend.db.base_class import Base


class Bid(Base):
    __tablename__ = 'bids'

    id = Column(Integer, Identity(), primary_key=True, index=True)
    apartment_id = Column(Integer, ForeignKey('apartments.id'))
    auction_id = Column(Integer, ForeignKey('auctions.id'))
    amount = Column(Integer, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
