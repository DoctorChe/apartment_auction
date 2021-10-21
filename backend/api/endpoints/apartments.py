from fastapi import APIRouter, Depends, Path, HTTPException
from sqlalchemy.orm import Session

from backend import schemas, crud
from backend.api.dependencies import get_db

router = APIRouter()


@router.post('/', response_model=schemas.Apartment, status_code=201)
def create_apartment(*, db: Session = Depends(get_db), payload: schemas.ApartmentIn):
    apartment = crud.create_apartment(db=db, apartment_in=payload)
    return apartment


@router.get('/{apartment_id}/', response_model=schemas.Apartment)
def read_apartment(*, db: Session = Depends(get_db), apartment_id: int = Path(..., gt=0)):
    apartment = crud.read_apartment(db=db, apartment_id=apartment_id)
    if not apartment:
        raise HTTPException(status_code=404, detail='Apartment not found')
    return apartment


@router.get('/', response_model=list[schemas.Apartment])
def read_all_apartments(db: Session = Depends(get_db)):
    return crud.read_all_apartments(db)


@router.put('/{apartment_id}/', response_model=schemas.Apartment)
def update_apartment(*, db: Session = Depends(get_db),
                     apartment_id: int = Path(..., gt=0), payload: schemas.Apartment):
    apartment = crud.read_apartment(db=db, apartment_id=apartment_id)
    if not apartment:
        raise HTTPException(status_code=404, detail='Apartment not found')
    apartment = crud.update_apartment(
        db=db, apartment=apartment,
        floor=payload.floor,
        area=payload.area,
        rooms=payload.rooms,
        start_price=payload.start_price,
        balcony=payload.balcony,
        finishing=payload.finishing,
        status=payload.status,
    )
    return apartment


@router.delete('/{apartment_id}/', response_model=schemas.Apartment)
def delete_apartment(*, db: Session = Depends(get_db), apartment_id: int = Path(..., gt=0)):
    apartment = crud.read_apartment(db=db, apartment_id=apartment_id)
    if not apartment:
        raise HTTPException(status_code=404, detail='Apartment not found')
    apartment = crud.delete_apartment(db=db, apartment_id=apartment_id)
    return apartment
