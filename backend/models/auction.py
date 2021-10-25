import datetime

from sqlalchemy import Column, Boolean, Integer, Identity, DateTime, func

from backend.db.base_class import Base


class Auction(Base):
    __tablename__ = 'auctions'

    id = Column(Integer, Identity(), primary_key=True, index=True)
    bid_duration = Column(Integer, nullable=False)
    time_start = Column(DateTime(timezone=True), server_default=func.now())
    time_last_bid = Column(DateTime(timezone=True))
    finished = Column(Boolean, default=False)

    @property
    def time_finish(self):
        if not self.time_last_bid:
            return self.time_start + datetime.timedelta(minutes=self.bid_duration)
        else:
            return self.time_last_bid + datetime.timedelta(minutes=self.bid_duration)

    @property
    def time_left(self):
        dt = self.time_finish - datetime.datetime.now(datetime.timezone.utc)
        # dt = divmod(dt.total_seconds(), 60)
        return dt
