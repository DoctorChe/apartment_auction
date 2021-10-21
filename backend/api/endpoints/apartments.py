from fastapi import APIRouter, Depends, Path, HTTPException
from sqlalchemy.orm import Session

from backend import schemas, crud
from backend.api.dependencies import get_db

router = APIRouter()


@router.post('/apartments/', response_model=schemas.Apartment, status_code=201)
def create_apartment(*, db: Session = Depends(get_db), payload: schemas.ApartmentIn):
    apartment = crud.create_apartment(db=db, apartment_in=payload)
    return apartment


@router.get('/apartments/{number}/', response_model=schemas.Apartment)
def read_apartment(*, db: Session = Depends(get_db), number: int = Path(..., gt=0)):
    apartment = crud.read_apartment(db=db, number=number)
    if not apartment:
        raise HTTPException(status_code=404, detail='Apartment not found')
    return apartment


@router.get('/apartments/', response_model=list[schemas.Apartment])
def read_all_apartments(db: Session = Depends(get_db)):
    return crud.read_all_apartments(db)
