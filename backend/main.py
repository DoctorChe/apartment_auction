from fastapi import FastAPI

from backend.api.endpoints import apartments, root

app = FastAPI()

app.include_router(apartments.router, prefix='/apartments', tags=['apartments'])
app.include_router(root.router)
