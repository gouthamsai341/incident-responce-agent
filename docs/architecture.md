# RecallOps Architecture

## Request path

User -> React -> FastAPI -> Incident Agent -> Hindsight Recall -> OpenRouter -> Recommendation.

## Learning path

Engineer action -> Outcome form -> FastAPI -> Hindsight Retain -> future Recall.

## Why Hindsight is core

RecallOps depends on Hindsight for persistent operational experience. The recommendation is grounded in retrieved historical incident evidence rather than a prompt-only response.

## Three Hindsight operations

- Retain: store incident and outcome experience.
- Recall: retrieve relevant historical experience.
- Reflect: reason over retained memories when needed.

The current MVP uses Recall directly for the OpenRouter recommendation path and exposes Hindsight Reflect in the memory service for deeper evidence-based reasoning.
