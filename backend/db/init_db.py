import json

from sqlalchemy.orm import Session

from backend.crud.apartments import create_apartments
from backend.db.base_class import Base
from backend.db.session import engine


def init_db(db: Session) -> None:
    Base.metadata.create_all(bind=engine)

    with open('./backend/db/apartments.json') as f:
        data = json.load(f)
    create_apartments(db, data)
