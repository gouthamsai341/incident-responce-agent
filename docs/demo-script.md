# RecallOps Demo Script

## 1. New incident

Enter:

- Payment API
- P1
- Payment API latency increased
- Latency 5.2s
- 30% requests timing out
- Database CPU increased

## 2. Show Hindsight memories

Point out that previous incidents are returned.

Highlight a successful index fix and a failed connection-pool-only fix.

## 3. Explain recommendation

The agent recommends checking the transaction query/index path because historical evidence shows a similar successful resolution.

## 4. Record outcome

Record:

Action: added missing index.

Result: latency dropped to 320ms.

Success: yes.

Feedback: check transaction-query indexes early.

## 5. Repeat

Submit a similar incident and show that the newly retained outcome becomes part of the historical evidence.
