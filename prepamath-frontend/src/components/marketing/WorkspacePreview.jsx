import ReactMarkdown from "react-markdown";
import remarkMath from "remark-math";
import rehypeKatex from "rehype-katex";
import "katex/dist/katex.min.css";

// A static snapshot of the real workspace — same classes/tokens as
// LeftPanel/RightPanel, same ReactMarkdown+KaTeX pipeline, real content from
// the ingested "Réduction des endomorphismes" chapter. Not a screenshot and
// not an interactive component: no fetches, no state, just what the actual
// product looks like, reused directly rather than approximated.
const LESSON_CONTENT = String.raw`Soit $\mathcal{B} = (\mathcal{B}_1, \dots, \mathcal{B}_p)$ une base adaptée à une décomposition $E = \bigoplus_{1 \leqslant i \leqslant p} E_i$.

L'endomorphisme $u$ stabilise chaque $E_i$ si, et seulement si, sa matrice dans la base $\mathcal{B}$ est diagonale par blocs.`;

const ANSWER_CONTENT = String.raw`Oui — ici, "stabiliser chaque $E_i$" veut dire que pour tout vecteur $x \in E_i$, son image $u(x)$ reste dans $E_i$. C'est exactement ce qui force la matrice à être diagonale par blocs : chaque bloc $A_i$ décrit l'action de $u$ **restreinte** à $E_i$, sans aucun mélange avec les autres sous-espaces.`;

export default function WorkspacePreview() {
  return (
    <div className="rounded-xl border border-border-subtle overflow-hidden grid grid-cols-1 md:grid-cols-2 h-[420px]">
      {/* Left: the lesson, exactly as LeftPanel renders it */}
      <div className="bg-surface border-b md:border-b-0 md:border-r border-border-subtle flex flex-col min-h-0">
        <div className="flex-shrink-0 px-4 py-3 border-b border-border-subtle text-sm font-semibold text-ink">
          Réduction des endomorphismes et des matrices carrées
        </div>
        <div className="flex-1 overflow-hidden p-4">
          <div className="prose prose-invert prose-sm max-w-none prose-p:text-ink prose-strong:text-ink">
            <span className="block text-lg font-bold text-accent-amber-text mb-2">Proposition 4</span>
            <ReactMarkdown remarkPlugins={[remarkMath]} rehypePlugins={[rehypeKatex]}>
              {LESSON_CONTENT}
            </ReactMarkdown>
          </div>
        </div>
      </div>

      {/* Right: the chat, exactly as RightPanel renders it */}
      <div className="bg-surface flex flex-col min-h-0">
        <div className="flex-shrink-0 px-4 py-3 border-b border-border-subtle text-sm font-semibold text-ink">
          KernelBot
        </div>
        <div className="flex-1 overflow-hidden p-4 space-y-3">
          <div className="p-3 rounded-md border bg-accent-violet-bg border-accent-violet-bg ml-8 text-sm text-ink">
            Pourquoi la matrice est diagonale par blocs ici ?
          </div>
          <div className="p-3 rounded-md border bg-surface border-border-subtle mr-8 text-sm">
            <div className="prose prose-invert prose-sm max-w-none prose-p:text-ink [&_p]:m-0">
              <ReactMarkdown remarkPlugins={[remarkMath]} rehypePlugins={[rehypeKatex]}>
                {ANSWER_CONTENT}
              </ReactMarkdown>
            </div>
            <div className="mt-2 pt-2 border-t border-border-subtle flex flex-wrap gap-1">
              <span className="text-xs font-medium text-accent-amber-text bg-accent-amber-bg px-2 py-0.5 rounded-full">
                Proposition 4
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
