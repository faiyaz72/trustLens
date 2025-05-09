from fastapi import APIRouter, Request

router = APIRouter()

@router.get("/ping")
def ping(request: Request):
    ipAddr = request.client.host
    return {"message": "pong", "ip": ipAddr}
