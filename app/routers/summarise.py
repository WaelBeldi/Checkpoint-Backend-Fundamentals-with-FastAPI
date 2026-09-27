from fastapi import APIRouter

from app.schemas.summarise import SummariseRequest
from app.services.summarise_service import generate_summary

router = APIRouter()


@router.post("/summarise")
def summarise(request: SummariseRequest):
    bullets = generate_summary(
        request.text,
        request.max_bullets
    )

    return {
        "summary": bullets,
        "bullet_count": len(bullets)
    }