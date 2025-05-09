from fastapi import APIRouter, HTTPException
from app.models.analyze_request import URLRequest
from app.services.article_analyzer import article_detail

router = APIRouter()

@router.post("/detail")
def detail(request: URLRequest):
    """
    Get article details by URL.
    """
    try:
        return article_detail(request.url)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

