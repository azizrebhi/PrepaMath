// Prerequisite graphs for the two separate "matières" of the CPGE MP
// 2nd-year program (Algèbre and Analyse are taught as distinct subjects,
// even across the same two semesters). Edges are real conceptual
// dependencies derived from the official program's own wording (e.g.
// "généralise celle vue en première année" for variables aléatoires needing
// familles sommables), not just chronological/semester order — a few
// chapters are genuine hubs that several later chapters build on.
//
// Unlike NeetCode's graph, sibling order here isn't "pick either" — the
// program is taught in a fixed sequence regardless of these dependencies.
// This graph answers "what should I re-read if I'm stuck on X", not
// "what can I unlock next".
//
// `match` is a substring (case-insensitive) matched against ingested
// Document.title values to decide whether a node is clickable.

export const ALGEBRE_GRAPH = {
  title: "Algèbre",
  nodes: [
    { id: "structures", title: "Structures algébriques usuelles", match: "structures algébriques", row: 0, col: 0, root: true },
    { id: "fonctions-vect", title: "Fonctions vectorielles, arcs paramétrés", match: "fonctions vectorielles", row: 0, col: 2, root: true },

    { id: "reduction", title: "Réduction des endomorphismes et des matrices carrées", match: "réduction des endomorphismes", row: 1, col: 0, parents: ["structures"] },
    { id: "calcul-diff", title: "Calcul différentiel", match: "calcul différentiel", row: 1, col: 2, parents: ["fonctions-vect"] },

    { id: "euclidiens", title: "Espaces préhilbertiens réels, endomorphismes des espaces euclidiens", match: "espaces préhilbertiens", row: 2, col: 0, parents: ["reduction"] },
    { id: "eq-diff", title: "Équations différentielles linéaires", match: "équations différentielles", row: 2, col: 1, parents: ["reduction", "fonctions-vect"] },
  ],
};

export const ANALYSE_GRAPH = {
  title: "Analyse",
  nodes: [
    { id: "topologie", title: "Topologie des espaces vectoriels normés", match: "espaces vectoriels normés", row: 0, col: 0, root: true },
    { id: "integration", title: "Intégration sur un intervalle quelconque", match: "intégration sur un intervalle", row: 0, col: 1, root: true },
    { id: "series-num", title: "Séries numériques", match: "séries numériques", row: 0, col: 2, root: true },
    { id: "familles-sommables", title: "Familles sommables de nombres complexes", match: "familles sommables", row: 0, col: 3, root: true },

    { id: "suites-series-fct", title: "Suites et séries de fonctions", match: "suites et séries de fonctions", row: 1, col: 0, parents: ["topologie"] },
    { id: "var-aleatoires", title: "Variables aléatoires discrètes", match: "variables aléatoires", row: 1, col: 3, parents: ["familles-sommables"] },

    { id: "integrales-param", title: "Intégrales à paramètre", match: "intégrales à paramètre", row: 2, col: 1, parents: ["integration", "suites-series-fct"] },
    { id: "series-entieres", title: "Séries entières", match: "séries entières", row: 2, col: 2, parents: ["suites-series-fct", "series-num"] },
  ],
};
