from fastapi import FastAPI

from backend.routers import router

app = FastAPI()

app.include_router(router)
