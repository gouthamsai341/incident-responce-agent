# RecallOps

RecallOps is an AI incident-response agent that turns previous production incidents into reusable operational experience.

## Core idea

When a new incident arrives:

1. RecallOps queries Hindsight for similar historical incidents.
2. The agent uses those memories as evidence.
3. OpenRouter generates a focused recommendation.
4. An engineer takes action.
5. The outcome is retained back into Hindsight.
6. Future incidents can use that outcome.

The key memory is not just `problem -> solution`. It captures attempted actions, success/failure, results, and engineer feedback.

## Architecture

```text
React + Tailwind-style UI
        |
        v
FastAPI
        |
        v
RecallOps Incident Agent
   |              |
   v              v
Hindsight      OpenRouter
Retain/Recall/Reflect
   |
   v
Operational outcome
   |
   v
Hindsight Retain
```

## Requirements

- Python 3.12+
- Node.js 20+
- Docker Desktop
- An OpenRouter API key
- An LLM API key for the Hindsight server

## 1. Start Hindsight

Copy the root environment example:

```powershell
Copy-Item .env.example .env
```

Or on macOS/Linux:

```bash
cp .env.example .env
```

Set `HINDSIGHT_LLM_API_KEY` in `.env`.

Then:

```bash
docker compose up -d hindsight
```

Hindsight API: http://localhost:8888  
Hindsight UI: http://localhost:9999

## 2. Configure backend

```bash
cd backend
python -m venv .venv
```

Windows:

```powershell
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

```bash
pip install -r requirements.txt
copy .env.example .env
```

Set `OPENROUTER_API_KEY` in `backend/.env`.

Run:

```bash
uvicorn app.main:app --reload --port 8000
```

## 3. Seed historical incidents

From the project root, with the backend virtual environment active:

```bash
python data/seed_incidents.py
```

## 4. Start frontend

```bash
cd frontend
npm install
copy .env.example .env
npm run dev
```

Open:

http://localhost:5173

## 5. Demo flow

First submit the seeded-style Payment API incident.

The agent should retrieve historical payment/database incidents.

Then record a successful outcome.

Submit a similar incident again.

The important demo moment is that the recommendation now has historical evidence and outcome context.

## Important

Hindsight must remain central to the project. Do not replace the memory layer with a normal vector database or a static JSON lookup.

Hindsight documentation:
https://hindsight.vectorize.io/

Hindsight GitHub:
https://github.com/vectorize-io/hindsight

Vectorize:
https://vectorize.io/
