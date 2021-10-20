from backend.core.logger_config import get_logger
from backend.db.init_db import init_db
from backend.db.session import SessionLocal

logger = get_logger(__name__)


def init() -> None:
    db = SessionLocal()
    init_db(db)


def main() -> None:
    logger.info('Creating initial data')
    init()
    logger.info('Initial data created')


if __name__ == '__main__':
    main()
