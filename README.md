# AI Mini API

A beginner-friendly backend API built with **FastAPI**.

The project provides four endpoints for health checking, chat, quiz generation, and text summarisation. The AI functionality currently uses **placeholder logic**, allowing the API to be developed and tested without an AI API key.

---

## 1. Project Goals

The goal of this project is to learn the fundamentals of building a clean and testable FastAPI backend.

The project demonstrates:

* FastAPI application setup
* GET and POST endpoints
* Pydantic request validation
* Structured JSON responses
* FastAPI routers
* Service-layer organization
* Swagger UI documentation
* Manual API testing
* Automated testing with pytest
* HTTPX for API testing
* Validation errors and HTTP status codes

---

## 2. Features

The API provides four endpoints:

| Method | Endpoint     | Description                           |
| ------ | ------------ | ------------------------------------- |
| GET    | `/health`    | Check whether the API is running      |
| POST   | `/chat`      | Send a message and receive an answer  |
| POST   | `/quiz`      | Generate quiz questions for a topic   |
| POST   | `/summarise` | Generate a short bullet-point summary |

The current implementation uses placeholder logic instead of a real AI model.

---

## 3. Project Structure

```text
fastapi-ai-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── health.py
│   │   ├── chat.py
│   │   ├── quiz.py
│   │   └── summarise.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── chat.py
│   │   ├── quiz.py
│   │   └── summarise.py
│   │
│   └── services/
│       ├── __init__.py
│       ├── chat_service.py
│       ├── quiz_service.py
│       └── summarise_service.py
│
├── tests/
│   ├── test_health.py
│   └── test_chat.py
│
├── docs/
│   └── api-test-report.md
│
├── requirements.txt
├── README.md
└── .gitignore
```

### Folder responsibilities

#### `app/`

Contains the FastAPI application.

#### `routers/`

Contains the API endpoints and HTTP-related logic.

#### `schemas/`

Contains Pydantic models used to validate incoming request data.

#### `services/`

Contains the application/business logic.

The placeholder AI logic is located here so it can later be replaced with a real AI service without changing the API structure.

#### `tests/`

Contains automated tests using pytest and HTTPX.

#### `docs/`

Contains additional project documentation and the API test report.

---

# 4. Requirements

Make sure you have:

* Python 3.10+
* pip
* A virtual environment

The project dependencies are listed in:

```text
requirements.txt
```

---

# 5. Installation

## Create the project

```bash
mkdir fastapi-ai-api
cd fastapi-ai-api
```

## Create a virtual environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

You should see:

```text
(venv)
```

at the beginning of your terminal prompt.

---

# 6. Install Dependencies

Install all required packages:

```bash
pip install -r requirements.txt
```

The main dependencies are:

```text
fastapi
uvicorn
pydantic
pytest
pytest-asyncio
httpx
```

---

# 7. Run the API

From the project root:

```bash
uvicorn app.main:app --reload
```

The API will start at:

```text
http://127.0.0.1:8000
```

You should see a message similar to:

```text
Uvicorn running on http://127.0.0.1:8000
```

---

# 8. Open the API

Open:

```text
http://127.0.0.1:8000
```

You should receive:

```json
{
    "message": "Welcome to AI Mini API",
    "docs": "/docs"
}
```

---

# 9. Swagger UI

FastAPI automatically generates interactive API documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

Swagger UI allows you to:

* See all available endpoints
* See request schemas
* See validation rules
* Send requests
* Inspect responses
* Test invalid requests

No additional API documentation tool is required.

---

# 10. API Endpoints

## GET `/health`

Checks whether the API is running.

This endpoint does not call an AI model.

### Request

```http
GET /health
```

### Response

```json
{
    "status": "ok",
    "version": "1.0.0",
    "timestamp": "2026-09-27T16:40:00+00:00"
}
```

The timestamp will change for every request.

### Status Code

```text
200 OK
```

---

# 11. POST `/chat`

Receives a message and returns a structured answer.

## Request

```http
POST /chat
```

### JSON Body

```json
{
    "message": "What is FastAPI?"
}
```

### Response

```json
{
    "answer": "This is a placeholder answer to your message: What is FastAPI?",
    "model": "placeholder"
}
```

### Validation

The `message` field:

* Is required
* Must be a string
* Minimum length: 1 character
* Maximum length: 2000 characters

### Invalid Request

```json
{
    "message": ""
}
```

Expected status:

```text
422 Unprocessable Entity
```

---

# 12. POST `/quiz`

Generates quiz questions for a specified topic.

## Request

```http
POST /quiz
```

### JSON Body

```json
{
    "topic": "Python",
    "number_of_questions": 3
}
```

### Response

```json
{
    "topic": "Python",
    "number_of_questions": 3,
    "questions": [
        {
            "id": 1,
            "question": "What is an important concept in Python?",
            "options": [
                "Concept A",
                "Concept B",
                "Concept C",
                "Concept D"
            ]
        }
    ]
}
```

The actual response contains the requested number of questions.

### Validation

The `topic` field:

* Is required
* Minimum length: 2 characters
* Maximum length: 100 characters

The `number_of_questions` field:

* Is required
* Must be an integer
* Minimum: 1
* Maximum: 20

### Invalid Request

```json
{
    "topic": "Python",
    "number_of_questions": 0
}
```

Expected status:

```text
422 Unprocessable Entity
```

---

# 13. POST `/summarise`

Generates a short summary from a text.

## Request

```http
POST /summarise
```

### JSON Body

```json
{
    "text": "FastAPI is a modern Python framework for building APIs. It uses Python type hints for validation. It also provides automatic API documentation.",
    "max_bullets": 2
}
```

### Response

```json
{
    "summary": [
        "FastAPI is a modern Python framework for building APIs",
        "It uses Python type hints for validation"
    ],
    "bullet_count": 2
}
```

The current implementation uses simple placeholder logic rather than a real AI summarisation model.

### Validation

The `text` field:

* Is required
* Minimum length: 10 characters
* Maximum length: 10000 characters

The `max_bullets` field:

* Is optional
* Default: 3
* Minimum: 1
* Maximum: 10

### Invalid Request

```json
{
    "text": "Hi",
    "max_bullets": 2
}
```

Expected status:

```text
422 Unprocessable Entity
```

---

# 14. Pydantic Validation

The API uses Pydantic models to validate incoming request bodies.

For example:

```python
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
```

This prevents invalid data from reaching the application logic.

For example:

```json
{
    "topic": "Python",
    "number_of_questions": 0
}
```

is rejected before the quiz service is executed.

FastAPI returns:

```text
422 Unprocessable Entity
```

with details about the validation error.

---

# 15. Automated Tests

The project uses:

* pytest
* pytest-asyncio
* HTTPX

HTTPX is used as the HTTP client for testing the FastAPI application.

The tests use `ASGITransport` to communicate directly with the FastAPI application without starting a real web server.

The testing flow is:

```text
pytest
   ↓
HTTPX AsyncClient
   ↓
ASGITransport
   ↓
FastAPI application
   ↓
Endpoint
   ↓
Response
```

---

# 16. Run the Tests

From the project root:

```bash
python -m pytest -v
```

Expected result:

```text
tests/test_chat.py::test_chat PASSED
tests/test_chat.py::test_chat_invalid_message PASSED
tests/test_health.py::test_health PASSED

3 passed
```

### Why use `python -m pytest`?

Using:

```bash
python -m pytest
```

ensures pytest runs using the current Python interpreter and virtual environment.

---

# 17. Automated Tests Included

## Health test

Tests:

```text
GET /health
```

It verifies:

* HTTP status is `200`
* `status` exists and equals `"ok"`
* `version` exists
* `timestamp` exists

## Chat test

Tests:

```text
POST /chat
```

It verifies:

* HTTP status is `200`
* `answer` exists
* `model` exists
* the model is `"placeholder"`

## Chat validation test

Tests an invalid request:

```json
{
    "message": ""
}
```

It verifies that FastAPI returns:

```text
422
```

---

# 18. Manual Testing

The API can also be manually tested using Swagger UI.

Open:

```text
http://127.0.0.1:8000/docs
```

### Valid `/chat` request

```json
{
    "message": "What is FastAPI?"
}
```

Expected:

```text
200 OK
```

### Invalid `/chat` request

```json
{
    "message": ""
}
```

Expected:

```text
422 Unprocessable Entity
```

These tests demonstrate both successful requests and Pydantic validation.

---

# 19. Test Report

A detailed API testing report is available at:

```text
docs/api-test-report.md
```

The report documents:

* Tested endpoints
* Valid requests
* Invalid requests
* Expected status codes
* Validation errors
* Automated tests
* Manual Swagger tests
* Test results

---

# 20. Current AI Implementation

The project currently uses placeholder logic.

For example, `/chat` does not call an external AI provider.

Instead:

```python
def generate_chat_answer(message: str) -> str:
    return (
        f"This is a placeholder answer to your message: "
        f"{message}"
    )
```

This allows the backend architecture and API to be developed without requiring:

* an AI API key
* an external AI service
* paid API usage

The same approach is used for the quiz and summarisation endpoints.

---

# 21. Architecture

The application separates responsibilities into different layers.

```text
Client
   │
   ▼
FastAPI Router
   │
   ▼
Pydantic Schema
   │
   ▼
Service
   │
   ▼
Placeholder Logic
   │
   ▼
JSON Response
```

For example:

```text
POST /chat
     │
     ▼
chat.py
     │
     ▼
ChatRequest
     │
     ▼
Pydantic validation
     │
     ▼
generate_chat_answer()
     │
     ▼
JSON response
```

This structure makes it possible to replace the placeholder logic with a real AI model later without redesigning the API.

---

# 22. Future Improvements

Possible future improvements include:

* Connect `/chat` to a real LLM
* Generate real AI-powered quizzes
* Generate real AI summaries
* Add response Pydantic models
* Add authentication
* Add database storage
* Add environment variables for API keys
* Add error handling for external AI APIs
* Add more automated tests
* Add API versioning
* Add deployment configuration

---

# 23. License

This project is intended for educational purposes.
