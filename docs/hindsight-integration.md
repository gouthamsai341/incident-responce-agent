# Hindsight Integration

The integration lives in:

`backend/app/hindsight/memory.py`

The three operations are:

```python
await client.aretain(...)
await client.arecall(...)
await client.areflect(...)
```

Retain stores incident outcomes.

Recall retrieves similar experiences.

Reflect can synthesize a reasoned answer from the memory bank.

This separation makes the memory system observable and testable.
