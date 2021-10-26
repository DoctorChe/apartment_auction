from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from backend import schemas, crud
from backend.api.dependencies import get_db
from backend.core.logger_config import get_logger

logger = get_logger(__name__)

router = APIRouter()


@router.post('/', response_model=schemas.Bid, status_code=201)
def create_auction(*, db: Session = Depends(get_db),
                   apartment_id: int = Query(..., gt=0),
                   amount: int = Query(..., gt=0)):
    return crud.create_bid(db=db, apartment_id=apartment_id, amount=amount)
