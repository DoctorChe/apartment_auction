import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from backend.logger_config import get_logger

SQLALCHEMY_DATABASE_URL = f"""postgresql+psycopg2://{os.getenv("POSTGRES_USER")}:{os.getenv("POSTGRES_PASSWORD")}@{os.getenv("POSTGRES_HOST")}:{os.getenv("POSTGRES_PORT")}/postgres"""

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

logger = get_logger(__name__)


def _test_connection():
    """ Проверка подключения SQLAlchemy к базе данных. """
    from sqlalchemy import MetaData, Table, Column, Integer

    def create_test_table(name: str) -> Table:
        table = Table(
            name, metadata_obj,
            Column("id", Integer, primary_key=True),
        )
        table.create(engine)
        logger.info(f"Test table \"{name}\" create successful.")

        return table

    logger.info("Start test connection to database.")
    metadata_obj = MetaData()

    table_name = "test_table"
    test_table = create_test_table(table_name)

    for t in metadata_obj.sorted_tables:
        logger.debug(t.name)

    test_table.drop(engine)
    logger.info(f"Test table \"{table_name}\" drop successful.")


if __name__ == '__main__':
    _test_connection()
