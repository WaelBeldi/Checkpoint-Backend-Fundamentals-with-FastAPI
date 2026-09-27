from fastapi import FastAPI

from app.routers import health, chat, quiz, summarise

app = FastAPI(
    title="AI Mini API",
    description="A beginner-friendly FastAPI backend",
    version="1.0.0"
)


app.include_router(health.router)
app.include_router(chat.router)
app.include_router(quiz.router)
app.include_router(summarise.router)

@app.get("/")
def root():
    return {
        "message": "Welcome to AI Mini API",
        "docs": "/docs"
    }