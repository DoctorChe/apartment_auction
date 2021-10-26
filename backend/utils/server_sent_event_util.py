import asyncio

from fastapi import Request

from backend.core.logger_config import get_logger

logger = get_logger(__name__)

MESSAGE_STREAM_DELAY = 1  # second
MESSAGE_STREAM_RETRY_TIMEOUT = 15000  # milisecond


def new_messages():
    return True


async def event_generator(bid_duration: int, request: Request):
    before_closing = bid_duration
    while True:
        # If client was closed the connection
        if await request.is_disconnected():
            break

        before_closing -= MESSAGE_STREAM_DELAY

        if before_closing < 0:
            logger.debug('Request completed. Disconnecting now')
            yield {
                "event": "end",
                "data": 'Auction is finished'
            }
            break

        # Checks for new messages and return them to client if any
        if new_messages():
            logger.info(f'Tik Tak Toe ({before_closing})')
            yield {
                "event": "update",
                "id": "message_id",
                "retry": MESSAGE_STREAM_RETRY_TIMEOUT,
                "data": before_closing
            }

        await asyncio.sleep(MESSAGE_STREAM_DELAY)
