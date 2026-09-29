import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

export default function RoadmapPage() {
  const [documents, setDocuments] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function fetchDocuments() {
      setLoading(true);
      setError(null);
      try {
        const res = await fetch(`${API_BASE_URL}/documents`);
        if (!res.ok) {
          throw new Error(`Request failed: ${res.status}`);
        }
        const data = await res.json();
        setDocuments(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    }

    fetchDocuments();
  }, []);

  return (
    <div className="p-8 max-w-2xl mx-auto text-neutral-100">
      <h1 className="text-2xl font-semibold mb-6">Chapters</h1>

      {loading && <p className="text-neutral-500">Loading...</p>}
      {error && <p className="text-red-400">Failed to load chapters: {error}</p>}

      {!loading && !error && documents.length === 0 && (
        <p className="text-neutral-500">No chapters ingested yet.</p>
      )}

      <div className="space-y-3">
        {documents.map((doc) => (
          <Link
            key={doc.id}
            to={`/chapter/${doc.id}`}
            className="block p-4 rounded-lg border border-neutral-800 bg-neutral-900 hover:border-neutral-600 transition-colors"
          >
            <div className="font-medium">{doc.title}</div>
            <div className="text-xs text-neutral-500 mt-1">{doc.status}</div>
          </Link>
        ))}
      </div>
    </div>
  );
}
