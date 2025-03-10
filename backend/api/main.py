from fastapi import APIRouter

from api.routes import info

api_router = APIRouter()
api_router.include_router(info.router,prefix="/api",tags=["info"])


