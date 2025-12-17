from fastapi import APIRouter
from app.schemas.round import RoundStateResponse

router = APIRouter()

@router.get("/ping", response_model= RoundStateResponse)
def ping_rounds():
    return {
        "state": "OK",
        "message": "rounds alive"
    }