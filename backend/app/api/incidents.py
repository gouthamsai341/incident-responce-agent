from fastapi import APIRouter
from app.models.incident import IncidentCreate, OutcomeCreate
from app.services.incident_service import create_incident, retain_outcome

router = APIRouter(prefix="/api/incidents", tags=["incidents"])

@router.post("")
async def create(payload: IncidentCreate):
    incident, recommendation, memories = await create_incident(payload)
    return {
        "incident": incident,
        "recommendation": recommendation,
        "memories": memories,
    }

@router.post("/outcome")
async def outcome(payload: OutcomeCreate):
    await retain_outcome(payload)
    return {"status": "stored", "message": "Incident outcome retained in Hindsight."}
