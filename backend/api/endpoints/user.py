from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from backend import schemas, crud
from backend.api.dependencies import get_db
from backend.core.logger_config import get_logger

logger = get_logger(__name__)

router = APIRouter()


@router.post('/sign-in', response_model=schemas.User)
def sign_in(*, db: Session = Depends(get_db),
            name: str = Query(...)):
    return crud.get_or_create_user(db=db, name=name)
