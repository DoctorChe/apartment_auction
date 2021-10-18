import pytest

from fastapi.testclient import TestClient
from httpx import AsyncClient

from backend.main import app


client = TestClient(app)


@pytest.mark.asyncio
async def test_docs():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/docs")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_read_root_async_client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello world! From FastAPI running on Uvicorn with Gunicorn. Using Python 3.9"
    }


def test_read_root_test_client():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello world! From FastAPI running on Uvicorn with Gunicorn. Using Python 3.9"
    }
