import ReactMarkdown from "react-markdown";
import remarkMath from "remark-math";
import rehypeKatex from "rehype-katex";
import "katex/dist/katex.min.css";

// Same KaTeX pipeline as WorkspacePreview, same tokens — a real formula
// rendered the same way the actual product renders one, not a decorative
// image. The Vandermonde matrix fits the subject: its determinant is the
// classic tool for showing eigenvectors tied to distinct eigenvalues are
// independent, a result straight out of the Réduction chapter itself.
const MATRIX = String.raw`$$
V = \begin{pmatrix}
1 & x_1 & x_1^2 & \cdots & x_1^{n-1} \\
1 & x_2 & x_2^2 & \cdots & x_2^{n-1} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & x_n & x_n^2 & \cdots & x_n^{n-1}
\end{pmatrix}
$$`;

const DETERMINANT = String.raw`$$\det V = \prod_{1 \leqslant i < j \leqslant n} (x_j - x_i)$$`;

export default function VandermondeVisual() {
  return (
    <div className="rounded-xl border border-border-subtle bg-surface p-8 flex flex-col items-center justify-center gap-4">
      <div className="prose prose-invert max-w-none prose-p:text-ink prose-p:m-0 [&_.katex]:text-ink [&_.katex-display]:my-0">
        <ReactMarkdown remarkPlugins={[remarkMath]} rehypePlugins={[rehypeKatex]}>
          {MATRIX}
        </ReactMarkdown>
      </div>
      <div className="h-px w-16 bg-border-subtle" />
      <div className="prose prose-invert max-w-none [&_.katex]:text-accent-amber-text [&_.katex-display]:my-0">
        <ReactMarkdown remarkPlugins={[remarkMath]} rehypePlugins={[rehypeKatex]}>
          {DETERMINANT}
        </ReactMarkdown>
      </div>
      <span className="text-xs text-ink-muted">Matrice de Vandermonde</span>
    </div>
  );
}
