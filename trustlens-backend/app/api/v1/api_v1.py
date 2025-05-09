from fastapi import APIRouter
from app.api.v1.endpoints import analyze
from app.api.v1.endpoints import test

api_router = APIRouter()
api_router.include_router(analyze.router, tags=["analyze"])
api_router.include_router(test.router, tags=["test"])