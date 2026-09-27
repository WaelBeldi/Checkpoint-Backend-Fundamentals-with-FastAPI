from pydantic import BaseModel, Field


class QuizRequest(BaseModel):
    topic: str = Field(
        ...,
        min_length=2,
        max_length=100
    )

    number_of_questions: int = Field(
        ...,
        ge=1,
        le=20
    )