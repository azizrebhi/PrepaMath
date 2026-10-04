import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import ReactMarkdown from "react-markdown";
import remarkMath from "remark-math";
import rehypeKatex from "rehype-katex";
import "katex/dist/katex.min.css";
import { useAuth } from "../../context/AuthContext";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

// Tailwind's preflight strips default list styling (no bullets/numbers,
// no indentation) — the model's answers use numbered lists, so restore
// just enough for them to read correctly.
const MARKDOWN_COMPONENTS = {
  ol: ({ node, ...props }) => <ol className="list-decimal pl-5 space-y-1" {...props} />,
  ul: ({ node, ...props }) => <ul className="list-disc pl-5 space-y-1" {...props} />,
};

export default function RightPanel({ selectedPartId, currentLessonChunkIds }) {
  const { chapterId } = useParams();
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [conversationId, setConversationId] = useState(null);
  const [loadingHistory, setLoadingHistory] = useState(true);
  const { token } = useAuth();

  // A conversation belongs to one chapter — restore it from the backend
  // (messages were already being persisted there; nothing was ever fetching
  // them back, which is why history vanished on every reload). Switching
  // sections within the same chapter should NOT touch this, which is why
  // this depends on chapterId only, not selectedPartId.
  useEffect(() => {
    let cancelled = false;

    async function loadConversation() {
      setLoadingHistory(true);
      try {
        const res = await fetch(`${API_BASE_URL}/documents/${chapterId}/conversation`, {
          headers: { Authorization: `Bearer ${token}` },
        });
        if (!res.ok) {
          throw new Error(`Échec de la requête : ${res.status}`);
        }
        const data = await res.json();
        if (cancelled) return;
        setConversationId(data.conversation_id);
        setMessages(data.messages.map((m) => ({ role: m.role, content: m.content })));
      } catch {
        if (!cancelled) {
          setMessages([]);
          setConversationId(null);
        }
      } finally {
        if (!cancelled) setLoadingHistory(false);
      }
    }

    loadConversation();
    return () => {
      cancelled = true;
    };
  }, [chapterId, token]);

  async function handleSubmit(e) {
    e.preventDefault();
    const query = input.trim();
    if (!query || loading || loadingHistory || !selectedPartId) return;

    setMessages((prev) => [...prev, { role: "user", content: query }]);
    setInput("");
    setLoading(true);
    setError(null);

    try {
      const res = await fetch(`${API_BASE_URL}/documents/${chapterId}/ask`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({
          query,
          current_part_id: selectedPartId,
          current_chunk_ids: currentLessonChunkIds,
          conversation_id: conversationId,
        }),
      });
      if (!res.ok) {
        throw new Error(`Échec de la requête : ${res.status}`);
      }
      const data = await res.json();
      setConversationId(data.conversation_id);
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
    <div className="flex flex-col h-full text-ink">
      <div className="flex-shrink-0 flex items-center justify-between border-b border-border-subtle p-4">
        <span className="font-semibold text-base">KernelBot</span>
        <span className="text-sm text-ink-muted">
          {loading ? "Réflexion en cours..." : "Statut : actif"}
        </span>
      </div>

      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {loadingHistory && (
          <p className="text-sm text-ink-muted">Chargement de la conversation...</p>
        )}

        {!loadingHistory && messages.length === 0 && (
          <p className="text-sm text-ink-muted">Pose une question sur ce chapitre.</p>
        )}

        {messages.map((m, i) => (
          <div
            key={i}
            className={`p-4 rounded-md border text-base ${
              m.role === "user"
                ? "bg-accent-violet-bg border-accent-violet-bg ml-8"
                : "bg-surface border-border-subtle mr-8"
            }`}
          >
            <div className="prose prose-invert max-w-none prose-p:text-ink prose-li:text-ink prose-strong:text-ink [&_p]:m-0">
              <ReactMarkdown
                remarkPlugins={[remarkMath]}
                rehypePlugins={[rehypeKatex]}
                components={MARKDOWN_COMPONENTS}
              >
                {m.content}
              </ReactMarkdown>
            </div>
            {m.sources && m.sources.length > 0 && (
              <div className="mt-2 pt-2 border-t border-border-subtle flex flex-wrap gap-1">
                {m.sources.map((s, j) => (
                  <span
                    key={j}
                    className="text-xs font-medium text-accent-amber-text bg-accent-amber-bg px-2 py-0.5 rounded-full"
                  >
                    {s.number ? `${s.chunk_type} ${s.number}` : s.chunk_type}
                  </span>
                ))}
              </div>
            )}
          </div>
        ))}

        {error && (
          <p className="text-sm text-accent-red-text">Échec de la réponse : {error}</p>
        )}
      </div>

      <form onSubmit={handleSubmit} className="flex-shrink-0 border-t border-border-subtle p-4">
        <div className="flex items-center gap-2">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Pose ta question sur ce chapitre..."
            disabled={loading || loadingHistory || !selectedPartId}
            className="flex-1 bg-canvas border border-border-subtle text-ink placeholder:text-ink-muted px-3 py-2.5 rounded-md outline-none text-base disabled:opacity-50"
          />
          <button
            type="submit"
            disabled={loading || loadingHistory || !input.trim() || !selectedPartId}
            className="bg-accent-amber-text text-[#18181a] font-medium px-4 py-2 rounded-md text-sm hover:bg-[#e6910d] disabled:opacity-40 disabled:cursor-not-allowed transition-colors"
          >
            Envoyer
          </button>
        </div>
      </form>
    </div>
  );
}
