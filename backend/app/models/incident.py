from datetime import datetime
from pydantic import BaseModel, Field

class IncidentCreate(BaseModel):
    service: str = Field(min_length=1)
    severity: str = "P2"
    title: str = Field(min_length=1)
    symptoms: list[str] = Field(default_factory=list)
    context: str = ""

class OutcomeCreate(BaseModel):
    incident_id: str
    action_taken: str
    result: str
    success: bool
    engineer_feedback: str = ""

class IncidentResponse(BaseModel):
    incident_id: str
    service: str
    severity: str
    title: str
    symptoms: list[str]
    recommendation: str
    reasoning: str
    memories: list[dict]
    created_at: datetime
