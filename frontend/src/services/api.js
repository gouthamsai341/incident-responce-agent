const API = import.meta.env.VITE_API_URL || "http://localhost:8000";

export async function createIncident(payload) {
  const response = await fetch(`${API}/api/incidents`, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(payload),
  });
  if (!response.ok) throw new Error(await response.text());
  return response.json();
}

export async function submitOutcome(payload) {
  const response = await fetch(`${API}/api/incidents/outcome`, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(payload),
  });
  if (!response.ok) throw new Error(await response.text());
  return response.json();
}
