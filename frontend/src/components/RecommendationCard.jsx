export default function RecommendationCard({ text }) {
  return (
    <section className="panel recommendation">
      <div className="panel-title">AI Recommendation</div>
      <pre>{text || "Submit an incident to generate a recommendation."}</pre>
    </section>
  );
}
