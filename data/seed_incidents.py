import json
import os
import asyncio
from hindsight_client import Hindsight

async def main():
    url = os.getenv("HINDSIGHT_URL", "http://localhost:8888")
    key = os.getenv("HINDSIGHT_API_KEY") or None
    bank = os.getenv("HINDSIGHT_BANK_ID", "recallops")
    client = Hindsight(base_url=url, api_key=key)

    with open("data/incidents.json", encoding="utf-8") as f:
        incidents = json.load(f)

    for item in incidents:
        content = f"""
Incident {item['incident_id']}
Service: {item['service']}
Severity: {item['severity']}
Title: {item['title']}
Symptoms: {', '.join(item['symptoms'])}
Investigation: {item['investigation']}
Action taken: {item['action_taken']}
Result: {item['result']}
Successful: {item['success']}
Engineer feedback: {item['engineer_feedback']}
"""
        await client.aretain(
            bank_id=bank,
            content=content,
            document_id=item["incident_id"],
            context="Historical production incident and outcome",
            tags=["incident", "outcome", "seed"],
        )
        print(f"Retained {item['incident_id']}")

if __name__ == "__main__":
    asyncio.run(main())
