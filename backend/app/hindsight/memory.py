from hindsight_client import Hindsight
from app.config import settings

class HindsightMemory:
    def __init__(self):
        self.client = Hindsight(
            base_url=settings.hindsight_url,
            api_key=settings.hindsight_api_key,
        )
        self.bank_id = settings.hindsight_bank_id

    async def retain_incident(self, incident_id: str, content: str):
        return await self.client.aretain(
            bank_id=self.bank_id,
            content=content,
            document_id=incident_id,
            context="RecallOps production incident",
            tags=["incident", "recallops"],
        )

    async def recall(self, query: str):
        response = await self.client.arecall(
            bank_id=self.bank_id,
            query=query,
        )
        return response.results or []

    async def reflect(self, query: str):
        response = await self.client.areflect(
            bank_id=self.bank_id,
            query=query,
            include_facts=True,
            budget="mid",
        )
        return response

memory = HindsightMemory()
