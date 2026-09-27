import pytest
from httpx import ASGITransport, AsyncClient

from app.main import app


@pytest.mark.asyncio
async def test_chat():
    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://127.0.0.1:8000"
    ) as client:

        response = await client.post(
            "/chat",
            json={
                "message": "What is FastAPI?"
            }
        )

    assert response.status_code == 200

    data = response.json()

    assert "answer" in data
    assert "model" in data
    assert data["model"] == "placeholder"