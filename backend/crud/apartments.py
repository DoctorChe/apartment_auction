from sqlalchemy.orm import Session

from backend import models, schemas
from backend.core.logger_config import get_logger

logger = get_logger(__name__)


def create_apartment(db: Session, apartment_in: schemas.ApartmentIn) -> schemas.Apartment:
    logger.info(apartment_in)
    classes = apartment_in.get('classes', {})
    balcony = True if 'C балконом' in classes else False
    finishing = True if 'С отделкой' in classes else False
    apartment = schemas.Apartment(**apartment_in, balcony=balcony, finishing=finishing)
    apartment_db = models.Apartment(**apartment.dict())
    db.add(apartment_db)
    db.commit()
    db.refresh(apartment_db)
    return apartment_db


def create_apartments(db: Session, apartments: list[schemas.ApartmentIn]) -> list[schemas.Apartment]:
    return [create_apartment(db, apartment_in=apartment) for apartment in apartments]
