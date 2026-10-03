import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import ChapterGraphView from "../components/roadmap/ChapterGraphView";
import { ALGEBRE_GRAPH, ANALYSE_GRAPH } from "../data/chapterGraphs";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

const GRAPHS_BY_SLUG = {
  algebre: ALGEBRE_GRAPH,
  analyse: ANALYSE_GRAPH,
};

export default function SubjectGraphPage() {
  const { subject } = useParams();
  const graph = GRAPHS_BY_SLUG[subject];
  const [documents, setDocuments] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const { token } = useAuth();

  useEffect(() => {
    async function fetchDocuments() {
      setLoading(true);
      setError(null);
      try {
        const res = await fetch(`${API_BASE_URL}/documents`, {
          headers: { Authorization: `Bearer ${token}` },
        });
        if (!res.ok) {
          throw new Error(`Échec de la requête : ${res.status}`);
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
  }, [token]);

  if (!graph) {
    return <p className="p-8 text-accent-red-text text-sm">Matière inconnue : {subject}</p>;
  }

  return (
    <div className="h-full overflow-y-auto p-8 text-ink">
      <div className="flex items-center gap-2 mb-6">
        {Object.entries(GRAPHS_BY_SLUG).map(([slug, g]) => (
          <Link
            key={slug}
            to={`/chapters/${slug}`}
            className={`text-sm px-3 py-1.5 rounded-md border transition-colors ${
              slug === subject
                ? "bg-accent-violet-bg border-accent-violet-bg text-accent-violet-text"
                : "bg-surface border-border-subtle text-ink-muted hover:text-ink"
            }`}
          >
            {g.title}
          </Link>
        ))}
      </div>

      {loading && <p className="text-ink-muted text-sm">Chargement...</p>}
      {error && (
        <p className="text-accent-red-text text-sm">Échec du chargement des chapitres : {error}</p>
      )}

      {!loading && !error && <ChapterGraphView graph={graph} documents={documents} />}
    </div>
  );
}
