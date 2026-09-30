import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { useAuth } from "../../context/AuthContext";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

export default function LeftPanel() {
  const { chapterId } = useParams();
  const [parts, setParts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const { token } = useAuth();

  useEffect(() => {
    async function fetchParts() {
      setLoading(true);
      setError(null);
      try {
        const res = await fetch(`${API_BASE_URL}/documents/${chapterId}/parts`, {
          headers: { Authorization: `Bearer ${token}` },
        });
        if (!res.ok) {
          throw new Error(`Échec de la requête : ${res.status}`);
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
  }, [chapterId, token]);

  if (loading) {
    return <p className="p-6 text-neutral-100">Chargement...</p>;
  }

  if (error) {
    return <p className="p-6 text-red-400">Échec du chargement : {error}</p>;
  }

  return (
    <div className="p-6 text-neutral-100">
      <ul className="space-y-2">
        {Array.isArray(parts) ? (
          parts.map((part) => (
            <li key={part.id} className="p-3 bg-neutral-900 border border-neutral-800 rounded">
              <div>{part.title}</div>
              <div className="text-xs text-neutral-500">Section {part.order_index}</div>
            </li>
          ))
        ) : (
          <p className="text-sm text-neutral-400">Réponse de l'API invalide.</p>
        )}
      </ul>
    </div>
  );
}
