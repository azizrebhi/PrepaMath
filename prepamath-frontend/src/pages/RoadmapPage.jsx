import { Link } from "react-router-dom";
import { ALGEBRE_GRAPH, ANALYSE_GRAPH } from "../data/chapterGraphs";

const SUBJECTS = [
  { slug: "algebre", graph: ALGEBRE_GRAPH },
  { slug: "analyse", graph: ANALYSE_GRAPH },
];

export default function RoadmapPage() {
  return (
    <div className="h-full flex items-center justify-center p-8 text-ink">
      <div className="flex gap-6">
        {SUBJECTS.map(({ slug, graph }) => (
          <Link
            key={slug}
            to={`/chapters/${slug}`}
            className="w-64 rounded-xl border border-border-subtle bg-surface px-6 py-8 text-center hover:border-ink-muted transition-colors"
          >
            <span className="text-lg font-semibold">{graph.title}</span>
          </Link>
        ))}
      </div>
    </div>
  );
}
