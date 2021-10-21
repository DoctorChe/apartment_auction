import json

from sqlalchemy.orm import Session

from backend import crud, schemas
from backend.db.base_class import Base
from backend.db.session import engine


def init_db(db: Session) -> None:
    Base.metadata.create_all(bind=engine)

    with open('./backend/db/apartments.json') as f:
        apartments = json.load(f)
    for apartment in apartments:
        apartment_in = schemas.ApartmentIn(**apartment)
        crud.create_apartment(db=db, apartment_in=apartment_in)
