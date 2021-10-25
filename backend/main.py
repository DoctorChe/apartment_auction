from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from backend.api.endpoints import apartments, root

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS] or ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(apartments.router, prefix='/apartments', tags=['apartments'])
app.include_router(root.router, tags=['Hello world!'])
