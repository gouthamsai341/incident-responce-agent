import { useState } from "react";

export default function OutcomeForm({ incidentId, onSubmit }) {
  const [action, setAction] = useState("Checked the transaction query and database indexes.");
  const [result, setResult] = useState("Added the missing index. Latency dropped from 5.2s to 320ms.");
  const [success, setSuccess] = useState(true);
  const [feedback, setFeedback] = useState("For similar incidents, check transaction-query indexes early.");

  async function submit(e) {
    e.preventDefault();
    await onSubmit({incident_id: incidentId, action_taken: action, result, success, engineer_feedback: feedback});
  }

  if (!incidentId) return null;

  return (
    <form className="panel" onSubmit={submit}>
      <div className="panel-title">Record Outcome</div>
      <label>Action<textarea value={action} onChange={e=>setAction(e.target.value)} /></label>
      <label>Result<textarea value={result} onChange={e=>setResult(e.target.value)} /></label>
      <label>Engineer feedback<textarea value={feedback} onChange={e=>setFeedback(e.target.value)} /></label>
      <label className="check"><input type="checkbox" checked={success} onChange={e=>setSuccess(e.target.checked)} /> Fix succeeded</label>
      <button>Store Outcome in Hindsight</button>
    </form>
  );
}
