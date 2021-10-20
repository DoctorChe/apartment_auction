from fastapi import FastAPI

from backend.api.endpoints import root

app = FastAPI()

app.include_router(root.router)
