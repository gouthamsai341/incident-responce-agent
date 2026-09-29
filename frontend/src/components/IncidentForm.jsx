import { useState } from "react";

export default function IncidentForm({ onSubmit, loading }) {
  const [form, setForm] = useState({
    service: "Payment API",
    severity: "P1",
    title: "Payment API latency increased",
    symptoms: "Latency 5.2s,30% requests timing out,Database CPU increased",
    context: "Production traffic increased shortly before the incident."
  });

  function update(key, value) {
    setForm({...form, [key]: value});
  }

  async function submit(e) {
    e.preventDefault();
    await onSubmit({
      ...form,
      symptoms: form.symptoms.split(",").map(s => s.trim()).filter(Boolean)
    });
  }

  return (
    <form className="panel" onSubmit={submit}>
      <div className="panel-title">New Incident</div>
      <label>Service<input value={form.service} onChange={e=>update("service",e.target.value)} /></label>
      <label>Severity<select value={form.severity} onChange={e=>update("severity",e.target.value)}>
        <option>P1</option><option>P2</option><option>P3</option>
      </select></label>
      <label>Title<input value={form.title} onChange={e=>update("title",e.target.value)} /></label>
      <label>Symptoms<textarea value={form.symptoms} onChange={e=>update("symptoms",e.target.value)} /></label>
      <label>Context<textarea value={form.context} onChange={e=>update("context",e.target.value)} /></label>
      <button disabled={loading}>{loading ? "Analyzing..." : "Analyze Incident"}</button>
    </form>
  );
}
