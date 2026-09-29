from datetime import datetime, timezone
from uuid import uuid4
from app.hindsight.memory import memory
from app.agents.incident_agent import analyze_incident

async def create_incident(payload):
    incident = {
        "incident_id": str(uuid4()),
        "service": payload.service,
        "severity": payload.severity,
        "title": payload.title,
        "symptoms": payload.symptoms,
        "context": payload.context,
        "created_at": datetime.now(timezone.utc).isoformat(),
    }

    recommendation, memories = await analyze_incident(incident)

    return incident, recommendation, memories

async def retain_outcome(payload):
    content = f"""
Incident outcome:
Incident ID: {payload.incident_id}
Action taken: {payload.action_taken}
Result: {payload.result}
Successful: {payload.success}
Engineer feedback: {payload.engineer_feedback}

This is an operational outcome from RecallOps. Future incident-response
recommendations should use this outcome as evidence. A successful fix is
evidence of what worked; an unsuccessful fix is evidence of what did not work.
"""
    return await memory.retain_incident(
        f"outcome-{payload.incident_id}",
        content,
    )
