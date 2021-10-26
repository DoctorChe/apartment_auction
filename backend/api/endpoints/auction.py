from fastapi import APIRouter, Depends, Path, Query, Request, HTTPException
from sqlalchemy.orm import Session
from sse_starlette.sse import EventSourceResponse

from backend import schemas, crud
from backend.api.dependencies import get_db
from backend.core.logger_config import get_logger
from backend.utils.server_sent_event_util import event_generator

logger = get_logger(__name__)

router = APIRouter()


@router.get('/stream')
async def message_stream(bid_duration: int, request: Request):
    return EventSourceResponse(event_generator(bid_duration, request))


@router.post('/', response_model=schemas.Auction, status_code=201)
def create_auction(*, db: Session = Depends(get_db), bid_duration: int = Query(..., gt=0, le=10)):
    return crud.create_auction(db=db, bid_duration=bid_duration)


@router.get('/connect/', response_model=schemas.Auction)
def read_last_not_finished(db: Session = Depends(get_db)):
    return crud.read_last_not_finished(db)


@router.get('/{auction_id}/', response_model=schemas.Auction)
def read_auction(*, db: Session = Depends(get_db), auction_id: int = Path(..., gt=0)):
    auction = crud.read_auction(db=db, auction_id=auction_id)
    if not auction:
        raise HTTPException(status_code=404, detail='Auction not found')
    return auction


@router.put('/{auction_id}/', response_model=schemas.Auction)
def update_auction(*, db: Session = Depends(get_db),
                   auction_id: int = Path(..., gt=0), payload: schemas.Auction):
    auction = crud.read_auction(db=db, auction_id=auction_id)
    if not auction:
        raise HTTPException(status_code=404, detail='Auction not found')
    auction = crud.update_auction(
        db=db, auction=auction,
        time_last_bid=payload.time_last_bid,
    )
    return auction
