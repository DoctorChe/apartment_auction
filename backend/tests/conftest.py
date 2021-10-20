from typing import Generator

import pytest

from fastapi.testclient import TestClient

from backend.db.session import SessionLocal
from backend.main import app


@pytest.fixture(scope="session")
def db() -> Generator:
    yield SessionLocal()


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c
