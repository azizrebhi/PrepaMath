import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

const STATUS_LABELS = {
  ready: "prêt",
  processing: "en cours de traitement",
};

export default function RoadmapPage() {
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

  return (
    <div className="p-8 max-w-2xl mx-auto text-neutral-100">
      <h1 className="text-2xl font-semibold mb-6">Chapitres</h1>

      {loading && <p className="text-neutral-500">Chargement...</p>}
      {error && (
        <p className="text-red-400">Échec du chargement des chapitres : {error}</p>
      )}

      {!loading && !error && documents.length === 0 && (
        <p className="text-neutral-500">Aucun chapitre disponible pour le moment.</p>
      )}

      <div className="space-y-3">
        {documents.map((doc) => (
          <Link
            key={doc.id}
            to={`/chapter/${doc.id}`}
            className="block p-4 rounded-lg border border-neutral-800 bg-neutral-900 hover:border-neutral-600 transition-colors"
          >
            <div className="font-medium">{doc.title}</div>
            <div className="text-xs text-neutral-500 mt-1">
              {STATUS_LABELS[doc.status] ?? doc.status}
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}
