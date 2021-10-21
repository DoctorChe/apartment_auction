from sqlalchemy.orm import Session

from backend import models, schemas
from backend.core.logger_config import get_logger

logger = get_logger(__name__)


def create_apartment(db: Session, apartment_in: schemas.ApartmentIn) -> schemas.Apartment:
    logger.info(apartment_in)
    classes = apartment_in.classes
    balcony = True if 'C балконом' in classes else False
    finishing = True if 'С отделкой' in classes else False
    apartment = schemas.Apartment(**apartment_in.dict(), balcony=balcony, finishing=finishing)
    apartment_db = models.Apartment(**apartment.dict())
    db.add(apartment_db)
    db.commit()
    db.refresh(apartment_db)
    return apartment_db


def create_apartments(db: Session, apartments: list[schemas.ApartmentIn]) -> list[schemas.Apartment]:
    return [create_apartment(db, apartment_in=apartment) for apartment in apartments]


def read_apartment(db: Session, number: int):
    return db.query(models.Apartment).filter(models.Apartment.number == number).first()


def read_all_apartments(db: Session):
    return db.query(models.Apartment).all()


def update_apartment(db: Session, apartment: models.Apartment,
                     floor: int, area: float, rooms: int, start_price: int, balcony: bool, finishing: bool):
    apartment.floor = floor
    apartment.area = area
    apartment.rooms = rooms
    apartment.start_price = start_price
    apartment.balcony = balcony
    apartment.finishing = finishing
    db.commit()
    return apartment


def delete_apartment(db: Session, number: int):
    apartment = db.query(models.Apartment).filter(models.Apartment.number == number).first()
    db.delete(apartment)
    db.commit()
    return apartment
