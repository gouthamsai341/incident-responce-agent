export default function MemoryCard({ memories }) {
  return (
    <section className="panel">
      <div className="panel-title">Hindsight Memories</div>
      {!memories?.length && <p className="muted">No memories retrieved yet.</p>}
      <div className="memory-list">
        {memories?.map((m, i) => (
          <div className="memory" key={i}>
            <span>Memory {i + 1}</span>
            <p>{m.text}</p>
          </div>
        ))}
      </div>
    </section>
  );
}
