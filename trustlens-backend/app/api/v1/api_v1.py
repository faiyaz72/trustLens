from fastapi import APIRouter
from app.api.v1.endpoints import analyze
from app.api.v1.endpoints import ping

api_router = APIRouter()
api_router.include_router(analyze.router, tags=["analyze"])
api_router.include_router(ping.router, tags=["test"])