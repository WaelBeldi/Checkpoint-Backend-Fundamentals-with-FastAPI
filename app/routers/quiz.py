from fastapi import APIRouter

from app.schemas.quiz import QuizRequest
from app.services.quiz_service import generate_quiz

router = APIRouter()


@router.post("/quiz")
def quiz(request: QuizRequest):
    questions = generate_quiz(
        request.topic,
        request.number_of_questions
    )

    return {
        "topic": request.topic,
        "number_of_questions": len(questions),
        "questions": questions
    }