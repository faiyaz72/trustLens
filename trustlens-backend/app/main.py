from fastapi import FastAPI
from app.api.v1.api_v1 import api_router

app = FastAPI(title="TrustLens API")

app.include_router(api_router, prefix="/api/v1")