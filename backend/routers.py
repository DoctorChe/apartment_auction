import sys

from fastapi import APIRouter


router = APIRouter()

version = f"{sys.version_info.major}.{sys.version_info.minor}"


@router.get("/")
async def read_root():
    message = f"Hello world! From FastAPI running on Uvicorn with Gunicorn. Using Python {version}"
    return {"message": message}
