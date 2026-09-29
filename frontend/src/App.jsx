import { useState } from "react";
import IncidentForm from "./components/IncidentForm";
import RecommendationCard from "./components/RecommendationCard";
import MemoryCard from "./components/MemoryCard";
import OutcomeForm from "./components/OutcomeForm";
import { createIncident, submitOutcome } from "./services/api";

export default function App() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");

  async function analyze(payload) {
    setLoading(true);
    setMessage("");
    try {
      setData(await createIncident(payload));
    } catch (e) {
      setMessage(e.message);
    } finally {
      setLoading(false);
    }
  }

  async function outcome(payload) {
    try {
      await submitOutcome(payload);
      setMessage("Outcome stored in Hindsight.");
    } catch (e) {
      setMessage(e.message);
    }
  }

  return (
    <main>
      <header>
        <div>
          <div className="eyebrow">INCIDENT COMMAND CENTER</div>
          <h1>RecallOps</h1>
          <p>Operational memory for faster incident response.</p>
        </div>
        <div className="status">● Hindsight memory enabled</div>
      </header>

      {message && <div className="notice">{message}</div>}

      <div className="grid">
        <div><IncidentForm onSubmit={analyze} loading={loading} /></div>
        <div>
          <RecommendationCard text={data?.recommendation} />
          <MemoryCard memories={data?.memories} />
          <OutcomeForm incidentId={data?.incident?.incident_id} onSubmit={outcome} />
        </div>
      </div>
    </main>
  );
}
