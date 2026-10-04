import { useEffect, useMemo, useState } from "react";
import { useParams } from "react-router-dom";
import ReactMarkdown from "react-markdown";
import remarkMath from "remark-math";
import rehypeKatex from "rehype-katex";
import { PanelLeft, X } from "lucide-react";
import "katex/dist/katex.min.css";
import { useApiFetch } from "../../context/AuthContext";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

// A numbered item (Définition 3, Proposition 1, ...) starts a new lesson;
// unnumbered items right after it (Exemple, Remarque, Point méthode) read as
// part of that same item in the source material, so they're folded into the
// same lesson rather than shown as their own standalone page. Exercices are
// filtered out before this runs — they're browsed separately.
function groupIntoLessons(chunks) {
  const lessons = [];
  let current = null;
  for (const chunk of chunks) {
    if (current === null || chunk.number !== null) {
      current = [chunk];
      lessons.push(current);
    } else {
      current.push(chunk);
    }
  }
  return lessons;
}

// Chunk content repeats its own "**Définition 3**"-style heading as its
// first line, and again right after "--- Solution (...) ---" when a
// solution was merged in at ingestion — both redundant once we're already
// showing the type+number as the lesson label, so strip both here rather
// than re-ingesting just for this. The heading in the source is sometimes
// pluralized ("Exemples" grouping several items under chunk_type "Exemple"),
// so the match allows an optional trailing "s".
function stripRedundantHeadings(content, chunkType, number) {
  const escType = chunkType.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  const escNumber = number ? number.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") : "";
  const headingPattern = `#{0,3}\\s*\\*{0,3}\\s*${escType}s?\\s*${escNumber}\\s*\\*{0,3}`;

  let cleaned = content.replace(
    new RegExp(`^(?:p\\.\\d+\\s+)?${headingPattern}\\s*\\n+`, "i"),
    ""
  );
  cleaned = cleaned.replace(
    new RegExp(`(---\\s*Solution\\s*\\([^)]*\\)\\s*---\\s*\\n+)${headingPattern}\\s*\\n+`, "i"),
    "$1"
  );
  return cleaned;
}

// \tag{n} needs KaTeX "display" mode, but this exact $$...$$ sometimes gets
// parsed as inline math when it's nested inside a list item in the source
// (remark-math's block-vs-inline detection depends on surrounding context,
// not just the $$ delimiters) — \quad (n) renders the same equation-number
// label in both modes, so swap it in rather than risk the hard KaTeX error.
function fixDisplayOnlyTags(content) {
  return content.replace(/\\tag\{([^}]*)\}/g, "\\quad ($1)");
}

// "Démonstration page 108" is a page pointer into the physical textbook —
// meaningless here since nothing is paginated, so it's dropped entirely
// (but "Démonstration non exigible", which is real content, is left alone).
// Two shapes show up in the source: standalone on its own line, and inline
// in brackets right after "Principe de démonstration." — e.g. "Principe de
// démonstration. [Démonstration page 109]" — the bracketed form needs a
// non-line-anchored match since it shares a line with real content before it.
function stripPageReferences(content) {
  let cleaned = content.replace(/^\s*\*{0,2}Démonstration\*{0,2}\s+page\s+\d+\.?\s*$/gim, "");
  cleaned = cleaned.replace(/\[\s*Démonstration\s+page\s+\d+\s*\]/gi, "");
  return cleaned;
}

// A chapter-section running header ("I Généralités", "*I Sous-espaces...*")
// is only noise when it stands alone on its own line — it's a page-break
// artifact from the source PDF that survived ingestion mid-chunk, not a real
// boundary (those were already clipped at ingestion time). Same shape the
// backend's own section detector matches, reused here as a safety net.
// Deliberately excludes the single-letter numerals "V" and "X" — in French
// math prose "X est un vecteur..." or "V est un sous-espace..." are ordinary
// sentences, and stripping them would corrupt real content.
function stripRunningHeaderArtifacts(content) {
  return content.replace(
    /^\s*\*{0,3}#{0,3}\*{0,3}\s*(?:I|II|III|IV|VI|VII|VIII|IX)\s+[A-ZÀ-Ý][^\n]*?\*{0,3}\s*$/gm,
    ""
  );
}

// "--- Solution (Proposition 1) ---" reads as plain body text otherwise —
// promote it to a real heading so typography actually sets it apart, and
// drop the "(Type N)" repeat since the badge above already says what this is.
function styleSolutionMarker(content) {
  return content.replace(/---\s*Solution\s*\([^)]*\)\s*---/gi, "\n#### Solution\n");
}

// Définitions, Corollaires and Propositions already get Tailwind Typography's
// native blockquote left-bar styling — but only when the source happened to
// wrap the statement in "> " markdown, which is inconsistent (e.g. most
// Propositions don't, even though Définitions usually do). Rather than
// adding a second, different-looking rule, make the existing one apply
// uniformly: if the statement isn't already quoted, quote it ourselves —
// just the formal claim itself, stopping before any proof sketch
// ("Principe de démonstration...") or merged-in solution.
const HIGHLIGHTED_TYPES = new Set(["Définition", "Corollaire", "Proposition"]);

function blockquoteStatement(content, chunkType) {
  if (!HIGHLIGHTED_TYPES.has(chunkType)) return content;
  if (/^\s*>/.test(content)) return content; // already quoted by the source

  const cutoffPatterns = [/Principe de démonstration/i, /Démonstration(?!s)[.\s]/i, /---\s*Solution\s*\(/i];
  const cutoffIndex = cutoffPatterns
    .map((re) => content.search(re))
    .filter((i) => i !== -1)
    .reduce((min, i) => Math.min(min, i), content.length);

  const statement = content.slice(0, cutoffIndex);
  const rest = content.slice(cutoffIndex);
  if (!statement.trim()) return content;

  const quoted = statement
    .split("\n")
    .map((line) => (line.trim() ? `> ${line}` : ">"))
    .join("\n");

  return `${quoted}\n${rest}`;
}

function cleanChunkContent(content, chunkType, number) {
  let cleaned = stripRedundantHeadings(content, chunkType, number);
  cleaned = stripPageReferences(cleaned);
  cleaned = stripRunningHeaderArtifacts(cleaned);
  cleaned = fixDisplayOnlyTags(cleaned);
  cleaned = blockquoteStatement(cleaned, chunkType);
  cleaned = styleSolutionMarker(cleaned);
  return cleaned;
}

function ChunkContent({ chunk }) {
  const label = chunk.number ? `${chunk.chunk_type} ${chunk.number}` : chunk.chunk_type;
  return (
    <div className="prose prose-invert max-w-none prose-p:text-ink prose-li:text-ink prose-strong:text-ink prose-headings:text-ink prose-h4:text-accent-green-text prose-h4:text-sm prose-h4:font-semibold prose-h4:mt-6 prose-h4:mb-2">
      <span className="block text-xl font-bold text-accent-amber-text mb-2">
        {label}
      </span>
      <ReactMarkdown remarkPlugins={[remarkMath]} rehypePlugins={[rehypeKatex]}>
        {cleanChunkContent(chunk.content, chunk.chunk_type, chunk.number)}
      </ReactMarkdown>
    </div>
  );
}

// Slides in from the right and overlays on top of the whole workspace (the
// regular page stays visible, dimmed, behind it) rather than pushing content
// over as an inline column — matches how NeetCode's own problem list panel
// behaves, which is what this was modeled on.
function SectionsDrawer({ parts, selectedPartId, setSelectedPartId, onClose }) {
  return (
    <>
      <div
        className="fixed inset-0 z-40 bg-black/60 animate-fade-in"
        onClick={onClose}
      />
      <div className="fixed inset-y-0 right-0 z-50 w-80 max-w-[85vw] bg-canvas border-l border-border-subtle overflow-y-auto shadow-2xl animate-slide-in-right">
        <div className="flex-shrink-0 flex items-center justify-between px-4 py-3 border-b border-border-subtle">
          <span className="text-sm font-medium text-ink-muted">Sections</span>
          <button
            onClick={onClose}
            className="text-ink-muted hover:text-ink transition-colors"
            aria-label="Fermer"
          >
            <X size={18} />
          </button>
        </div>
        <div className="pb-2">
          {parts.map((part, i) => {
            const active = part.id === selectedPartId;
            return (
              <button
                key={part.id}
                onClick={() => {
                  setSelectedPartId(part.id);
                  onClose();
                }}
                className={`w-full text-left flex gap-2.5 px-4 py-2.5 text-sm leading-snug transition-colors ${
                  active
                    ? "bg-accent-violet-bg text-accent-violet-text"
                    : "text-ink-muted hover:bg-surface-raised hover:text-ink"
                }`}
              >
                <span className="text-ink-muted shrink-0">{i + 1}.</span>
                <span>{part.title}</span>
              </button>
            );
          })}
        </div>
      </div>
    </>
  );
}

function ExercisesModal({ exercises, activeId, setActiveId, onClose }) {
  const active = exercises.find((e) => e.id === activeId) ?? null;

  return (
    <div className="absolute inset-0 z-10 bg-surface flex flex-col">
      <div className="flex-shrink-0 flex items-center justify-between p-4 border-b border-border-subtle">
        <span className="font-sans font-semibold text-base text-ink">Exercices de cette section</span>
        <button
          onClick={onClose}
          className="text-xs px-3 py-1.5 rounded-md border border-border-subtle text-ink-muted hover:border-ink-muted hover:text-ink transition-colors"
        >
          Fermer
        </button>
      </div>

      <div className="flex-shrink-0 p-4 border-b border-border-subtle overflow-x-auto">
        <div className="flex gap-2">
          {exercises.map((ex) => (
            <button
              key={ex.id}
              onClick={() => setActiveId(ex.id)}
              className={`text-xs px-3 py-1.5 rounded-md whitespace-nowrap border transition-colors ${
                ex.id === activeId
                  ? "bg-accent-violet-bg border-accent-violet-bg text-accent-violet-text"
                  : "bg-surface border-border-subtle text-ink-muted hover:text-ink"
              }`}
            >
              Exercice {ex.number}
            </button>
          ))}
        </div>
      </div>

      <div className="flex-1 overflow-y-auto p-4">
        {active ? (
          <ChunkContent chunk={active} />
        ) : (
          <p className="text-sm text-ink-muted">Choisis un exercice ci-dessus.</p>
        )}
      </div>
    </div>
  );
}

export default function LeftPanel({ selectedPartId, setSelectedPartId, setCurrentLessonChunkIds }) {
  const { chapterId } = useParams();
  const [parts, setParts] = useState([]);
  const [chunks, setChunks] = useState([]);
  const [lessonIndex, setLessonIndex] = useState(0);
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [showExercises, setShowExercises] = useState(false);
  const [activeExerciseId, setActiveExerciseId] = useState(null);
  const [loadingParts, setLoadingParts] = useState(true);
  const [loadingChunks, setLoadingChunks] = useState(false);
  const [error, setError] = useState(null);
  const apiFetch = useApiFetch();

  useEffect(() => {
    async function fetchParts() {
      setLoadingParts(true);
      setError(null);
      try {
        const res = await apiFetch(`${API_BASE_URL}/documents/${chapterId}/parts`);
        if (!res.ok) {
          throw new Error(`Échec de la requête : ${res.status}`);
        }
        const data = await res.json();
        setParts(data);
        if (data.length > 0) {
          setSelectedPartId(data[0].id);
        }
      } catch (err) {
        setError(err.message);
      } finally {
        setLoadingParts(false);
      }
    }

    fetchParts();
  }, [chapterId, apiFetch]);

  useEffect(() => {
    if (!selectedPartId) return;

    async function fetchChunks() {
      setLoadingChunks(true);
      setError(null);
      try {
        const res = await apiFetch(
          `${API_BASE_URL}/documents/${chapterId}/parts/${selectedPartId}/chunks`
        );
        if (!res.ok) {
          throw new Error(`Échec de la requête : ${res.status}`);
        }
        const data = await res.json();
        setChunks(data.chunks);
        setLessonIndex(0);
        setShowExercises(false);
        setActiveExerciseId(null);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoadingChunks(false);
      }
    }

    fetchChunks();
  }, [chapterId, selectedPartId, apiFetch]);

  const courseChunks = useMemo(
    () => chunks.filter((c) => c.chunk_type !== "Exercice"),
    [chunks]
  );
  const exerciseChunks = useMemo(
    () => chunks.filter((c) => c.chunk_type === "Exercice"),
    [chunks]
  );
  const lessons = useMemo(() => groupIntoLessons(courseChunks), [courseChunks]);
  const currentLesson = lessons[lessonIndex] ?? [];

  // Tell RightPanel exactly which chunks are on screen — narrower than the
  // whole part, so questions get answered against the specific lesson
  // being read rather than the entire (sometimes 30-50 chunk) section.
  useEffect(() => {
    setCurrentLessonChunkIds((lessons[lessonIndex] ?? []).map((c) => c.id));
  }, [lessonIndex, lessons, setCurrentLessonChunkIds]);

  if (loadingParts) {
    return <p className="p-6 text-ink-muted text-sm">Chargement...</p>;
  }

  if (error) {
    return <p className="p-6 text-accent-red-text text-sm">Échec du chargement : {error}</p>;
  }

  const currentPart = parts.find((p) => p.id === selectedPartId) ?? null;

  return (
    <div className="relative flex h-full text-ink">
      <div className="flex-1 flex flex-col min-w-0">
        <div className="flex-shrink-0 flex items-center gap-3 border-b border-border-subtle p-4">
          <button
            onClick={() => setSidebarOpen(true)}
            className="flex-shrink-0 text-ink-muted hover:text-ink transition-colors"
            aria-label="Afficher les sections"
          >
            <PanelLeft size={18} />
          </button>

          <span className="flex-1 min-w-0 text-base font-semibold truncate">{currentPart?.title}</span>

          {exerciseChunks.length > 0 && (
            <button
              onClick={() => {
                setShowExercises(true);
                setActiveExerciseId(exerciseChunks[0].id);
              }}
              className="flex-shrink-0 text-xs font-medium px-3 py-1.5 rounded-md bg-accent-amber-text text-[#18181a] hover:bg-[#a3835f] transition-colors whitespace-nowrap"
            >
              Exercices ({exerciseChunks.length})
            </button>
          )}
        </div>

        <div className="flex-1 overflow-y-auto p-6">
          {loadingChunks && (
            <p className="text-ink-muted text-sm">Chargement de la section...</p>
          )}

          {!loadingChunks && lessons.length === 0 && (
            <p className="text-ink-muted text-sm">Aucun contenu de cours pour cette section.</p>
          )}

          {!loadingChunks && lessons.length > 0 && (
            <div className="space-y-8 max-w-2xl">
              {currentLesson.map((chunk) => (
                <ChunkContent key={chunk.id} chunk={chunk} />
              ))}
            </div>
          )}
        </div>

        {!loadingChunks && lessons.length > 0 && (
          <div className="flex-shrink-0 flex items-center justify-between border-t border-border-subtle p-3">
            <button
              onClick={() => setLessonIndex((i) => Math.max(0, i - 1))}
              disabled={lessonIndex === 0}
              className="text-xs px-3 py-1.5 rounded-md border border-border-subtle text-ink-muted hover:border-ink-muted hover:text-ink transition-colors disabled:opacity-40 disabled:hover:border-border-subtle disabled:hover:text-ink-muted"
            >
              Précédent
            </button>
            <span className="font-mono text-[11px] text-ink-muted">
              Leçon {lessonIndex + 1} / {lessons.length}
            </span>
            <button
              onClick={() => setLessonIndex((i) => Math.min(lessons.length - 1, i + 1))}
              disabled={lessonIndex === lessons.length - 1}
              className="text-xs px-3 py-1.5 rounded-md border border-border-subtle text-ink-muted hover:border-ink-muted hover:text-ink transition-colors disabled:opacity-40 disabled:hover:border-border-subtle disabled:hover:text-ink-muted"
            >
              Suivant
            </button>
          </div>
        )}
      </div>

      {showExercises && (
        <ExercisesModal
          exercises={exerciseChunks}
          activeId={activeExerciseId}
          setActiveId={setActiveExerciseId}
          onClose={() => setShowExercises(false)}
        />
      )}

      {sidebarOpen && (
        <SectionsDrawer
          parts={parts}
          selectedPartId={selectedPartId}
          setSelectedPartId={setSelectedPartId}
          onClose={() => setSidebarOpen(false)}
        />
      )}
    </div>
  );
}
