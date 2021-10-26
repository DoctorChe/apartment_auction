from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from backend.api.endpoints import apartments, auction, bid, user, root
from backend.core.config import settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS] or ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(apartments.router, prefix='/apartments', tags=['apartments'])
app.include_router(auction.router, prefix='/auctions', tags=['auction'])
app.include_router(bid.router, prefix='/bids', tags=['bids'])
app.include_router(user.router, prefix='/auth', tags=['auth'])
app.include_router(root.router, tags=['Hello world!'])
