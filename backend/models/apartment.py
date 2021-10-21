from sqlalchemy import Column, Integer, Float, Boolean, String

from backend.db.base_class import Base


class Apartment(Base):
    __tablename__ = 'apartments'

    number = Column(Integer, primary_key=True, index=True)
    floor = Column(Integer, nullable=False)
    area = Column(Float, nullable=False)
    rooms = Column(Integer, nullable=False)
    balcony = Column(Boolean, nullable=False)
    finishing = Column(Boolean, nullable=False)
    start_price = Column(Integer, nullable=False)
    status = Column(String, nullable=False)
