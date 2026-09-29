import { useState } from "react";
import { useParams } from "react-router-dom";
import ReactMarkdown from "react-markdown";
import remarkMath from "remark-math";
import rehypeKatex from "rehype-katex";
import "katex/dist/katex.min.css";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

// Tailwind's preflight strips default list styling (no bullets/numbers,
// no indentation) — the model's answers use numbered lists, so restore
// just enough for them to read correctly.
const MARKDOWN_COMPONENTS = {
  ol: ({ node, ...props }) => <ol className="list-decimal pl-5 space-y-1" {...props} />,
  ul: ({ node, ...props }) => <ul className="list-disc pl-5 space-y-1" {...props} />,
};

export default function RightPanel() {
  const { chapterId } = useParams();
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  async function handleSubmit(e) {
    e.preventDefault();
    const query = input.trim();
    if (!query || loading) return;

    setMessages((prev) => [...prev, { role: "user", content: query }]);
    setInput("");
    setLoading(true);
    setError(null);

    try {
      const res = await fetch(`${API_BASE_URL}/documents/${chapterId}/ask`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query }),
      });
      if (!res.ok) {
        throw new Error(`Échec de la requête : ${res.status}`);
      }
      const data = await res.json();
      setMessages((prev) => [
        ...prev,
        { role: "assistant", content: data.answer, sources: data.sources },
      ]);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="flex flex-col h-full text-neutral-100">
      <div className="flex-shrink-0 flex items-center justify-between border-b border-neutral-800 p-4">
        <span>Tuteur IA</span>
        <span className="text-xs text-neutral-500">
          {loading ? "Réflexion en cours..." : "Statut : actif"}
        </span>
      </div>

      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {messages.length === 0 && (
          <p className="text-sm text-neutral-500">Pose une question sur ce chapitre.</p>
        )}

        {messages.map((m, i) => (
          <div
            key={i}
            className={`p-3 rounded border text-sm ${
              m.role === "user"
                ? "bg-neutral-800 border-neutral-700 ml-8"
                : "bg-neutral-900 border-neutral-800 mr-8"
            }`}
          >
            <div className="prose-sm prose-invert max-w-none [&_p]:m-0">
              <ReactMarkdown
                remarkPlugins={[remarkMath]}
                rehypePlugins={[rehypeKatex]}
                components={MARKDOWN_COMPONENTS}
              >
                {m.content}
              </ReactMarkdown>
            </div>
            {m.sources && m.sources.length > 0 && (
              <div className="mt-2 pt-2 border-t border-neutral-800 flex flex-wrap gap-1">
                {m.sources.map((s, j) => (
                  <span
                    key={j}
                    className="text-xs text-neutral-500 bg-neutral-950 px-2 py-0.5 rounded"
                  >
                    {s.number ? `${s.chunk_type} ${s.number}` : s.chunk_type}
                  </span>
                ))}
              </div>
            )}
          </div>
        ))}

        {error && (
          <p className="text-sm text-red-400">Échec de la réponse : {error}</p>
        )}
      </div>

      <form onSubmit={handleSubmit} className="flex-shrink-0 border-t border-neutral-800 p-4">
        <div className="flex items-center gap-2">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Pose ta question sur ce chapitre..."
            disabled={loading}
            className="flex-1 bg-neutral-900 border border-neutral-800 p-2 rounded outline-none text-sm disabled:opacity-50"
          />
          <button
            type="submit"
            disabled={loading || !input.trim()}
            className="bg-neutral-800 border border-neutral-700 px-4 py-2 rounded text-sm hover:bg-neutral-700 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            Envoyer
          </button>
        </div>
      </form>
    </div>
  );
}
