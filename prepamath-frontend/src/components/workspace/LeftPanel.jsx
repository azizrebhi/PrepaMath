import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

export default function LeftPanel() {
  const { chapterId } = useParams();
  const [parts, setParts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function fetchParts() {
      setLoading(true);
      setError(null);
      try {
        const res = await fetch(`${API_BASE_URL}/documents/${chapterId}/parts`);
        if (!res.ok) {
          throw new Error(`Request failed: ${res.status}`);
        }
        const data = await res.json();
        setParts(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    }

    fetchParts();
  }, [chapterId]); // re-fetch if the user navig

  // TODO 1: loading branch — return something simple, e.g. <p className="p-6">Loading...</p>
  if (loading) {
    return <p className="p-6 text-neutral-100">Loading...</p>;
  }

  // TODO 2: error branch — return something showing `error` to the user,
  // e.g. <p className="p-6 text-red-400">Failed to load: {error}</p>
  if (error) {
    return <p className="p-6 text-red-400">Failed to load: {error}</p>;
  }

  return (
    <div className="p-6 text-neutral-100">
      {/* TODO 3: you now have a real `parts` ar
          { id, title, order_index } objects. Render them — a plain
          <ul> mapping over parts, showing part.
          is a section-navigator list for now, not final section content
          (that needs a backend endpoint that doesn't exist yet — next
          conversation). */}
      <ul className="space-y-2">
  {Array.isArray(parts) ? (
    parts.map((part) => (
      <li key={part.id} className="p-3 bg-neutral-900 border border-neutral-800 rounded">
        <div>{part.title}</div>
        <div className="text-xs text-neutral-500">Order: {part.order_index}</div>
      </li>
    ))
  ) : (
    <p className="text-sm text-neutral-400">No parts array structure found in API response.</p>
  )}
</ul>

    </div>
  );
}
