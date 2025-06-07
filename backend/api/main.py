from fastapi import APIRouter

from api.routes import info
from api.routes import calc
from api.routes import openapi

api_router = APIRouter()
api_router.include_router(info.router,prefix="/api",tags=["info"])
api_router.include_router(calc.router,prefix="/api",tags=["calc"])
api_router.include_router(openapi.router,prefix="/api/openapi",tags=["openapi"])
