from fastapi import APIRouter

from app.schemas.chat import ChatRequest
from app.services.chat_service import generate_chat_answer

router = APIRouter()


@router.post("/chat")
def chat(request: ChatRequest):
    answer = generate_chat_answer(request.message)

    return {
        "answer": answer,
        "model": "placeholder"
    }