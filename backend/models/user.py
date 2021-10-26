from sqlalchemy import Column, Integer, Identity, String

from backend.db.base_class import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Identity(), primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
