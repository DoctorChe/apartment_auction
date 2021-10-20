from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend import schemas, crud
from backend.api.dependencies import get_db

router = APIRouter()


@router.post('/apartments/', response_model=schemas.Apartment, status_code=201)
def create_apartment(*, db: Session = Depends(get_db), payload: schemas.ApartmentIn):
    apartment = crud.create_apartment(db=db, apartment_in=payload)
    return apartment
