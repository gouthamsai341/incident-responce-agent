from app.hindsight.memory import memory
from app.llm.openrouter import generate

def _memory_text(items) -> str:
    if not items:
        return "No relevant historical incidents were found."
    lines = []
    for i, item in enumerate(items[:8], 1):
        text = getattr(item, "text", str(item))
        lines.append(f"{i}. {text}")
    return "\n".join(lines)

async def analyze_incident(incident: dict):
    query = (
        f"Production incident for service {incident['service']}: "
        f"{incident['title']}. Symptoms: {', '.join(incident['symptoms'])}. "
        f"Context: {incident['context']}. Find similar incidents, successful fixes, "
        f"failed fixes, and engineer lessons."
    )

    memories = await memory.recall(query)

    evidence = _memory_text(memories)

    prompt = f"""
Current incident:
Service: {incident['service']}
Severity: {incident['severity']}
Title: {incident['title']}
Symptoms: {incident['symptoms']}
Context: {incident['context']}

Historical evidence from Hindsight:
{evidence}

Produce:
1. Recommended first investigation/action.
2. Why this is relevant to the historical evidence.
3. What should NOT be repeated if a historical fix failed.
4. A short confidence statement based only on the available evidence.
"""
    recommendation = await generate(prompt)

    return recommendation, [
        {"text": getattr(item, "text", str(item)),
         "type": getattr(item, "type", "memory")}
        for item in memories[:8]
    ]
