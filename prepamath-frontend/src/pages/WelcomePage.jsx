import { Link } from "react-router-dom";
import WorkspacePreview from "../components/marketing/WorkspacePreview";
import VandermondeVisual from "../components/marketing/VandermondeVisual";
import ChapterGraphView from "../components/roadmap/ChapterGraphView";
import { ALGEBRE_GRAPH } from "../data/chapterGraphs";

export default function WelcomePage() {
  return (
    <div className="h-full overflow-y-auto">
      <div className="max-w-5xl mx-auto px-6 py-20">
        <div className="flex flex-col md:flex-row items-center gap-10">
          <div className="flex-1">
            <h1 className="text-4xl md:text-5xl font-bold tracking-tight leading-[1.1]">
              Pose ta question. Kernel connaît ta leçon.
            </h1>

            <p className="mt-6 text-ink-muted text-lg leading-relaxed">
              Réduction des endomorphismes, espaces vectoriels normés, et la suite
              du programme MP — un tuteur qui répond à partir de la leçon
              affichée à l'écran, pas d'un vague résumé du chapitre.
            </p>

            <Link
              to="/chapters"
              className="inline-block mt-8 px-6 py-3 rounded-lg bg-accent-amber-text text-[#18181a] font-medium hover:bg-[#a3835f] transition-colors"
            >
              Voir les chapitres
            </Link>
          </div>

          <div className="flex-1 w-full max-w-sm">
            <VandermondeVisual />
          </div>
        </div>

        <div className="mt-28">
          <WorkspacePreview />
        </div>

        <div className="mt-24">
          <h2 className="text-2xl font-semibold text-ink">Construit sur le vrai programme</h2>
          <p className="mt-2 text-ink-muted max-w-2xl">
            Chaque chapitre est relié à ceux dont il dépend réellement —
            pas une simple liste chronologique.
          </p>
          <div className="mt-6 h-[420px] rounded-xl border border-border-subtle overflow-hidden">
            <ChapterGraphView graph={ALGEBRE_GRAPH} documents={[]} />
          </div>
        </div>
      </div>
    </div>
  );
}
