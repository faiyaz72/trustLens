from fastapi import APIRouter, HTTPException
from app.models.analyze_request import URLRequest
from app.services.article_analyzer import analyze_article

router = APIRouter()

@router.post("/analyze")
def analyze(request: URLRequest):
    try:
        return analyze_article(request.url)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))