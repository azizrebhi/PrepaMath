import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { useApiFetch } from "../context/AuthContext";
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
  const [error, setError] = useState(null);
  const apiFetch = useApiFetch();

  useEffect(() => {
    async function fetchDocuments() {
      setError(null);
      try {
        const res = await apiFetch(`${API_BASE_URL}/documents`);
        if (!res.ok) {
          throw new Error(`Échec de la requête : ${res.status}`);
        }
        const data = await res.json();
        setDocuments(data);
      } catch (err) {
        setError(err.message);
      }
    }

    fetchDocuments();
  }, [apiFetch]);

  if (!graph) {
    return <p className="p-8 text-accent-red-text text-sm">Matière inconnue : {subject}</p>;
  }

  return (
    <div className="relative h-full text-ink">
      {/* The graph's own canvas spans the full page — its dot background
          pans and zooms together with the nodes, which is what makes
          panning feel continuous instead of the content clipping against a
          static backdrop that doesn't move with it. */}
      <div className="absolute inset-0">
        <ChapterGraphView graph={graph} documents={documents} />
      </div>

      <div className="absolute top-4 left-4 z-10 flex items-center gap-2">
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

      {error && (
        <p className="absolute top-4 right-4 z-10 text-sm text-accent-red-text bg-surface border border-border-subtle rounded-md px-3 py-1.5">
          Échec du chargement des chapitres : {error}
        </p>
      )}
    </div>
  );
}
