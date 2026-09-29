import httpx
from app.config import settings

async def generate(prompt: str) -> str:
    headers = {
        "Authorization": f"Bearer {settings.openrouter_api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:5173",
        "X-Title": "RecallOps",
    }
    payload = {
        "model": settings.openrouter_model,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are RecallOps, an incident-response assistant. "
                    "Use the supplied historical evidence. Never invent an incident "
                    "or claim a fix succeeded unless the evidence says so."
                ),
            },
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.2,
    }
    async with httpx.AsyncClient(timeout=60) as client:
        response = await client.post(
            f"{settings.openrouter_base_url}/chat/completions",
            headers=headers,
            json=payload,
        )
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]
