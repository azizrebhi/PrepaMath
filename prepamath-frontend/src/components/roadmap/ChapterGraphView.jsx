import { useMemo } from "react";
import { useNavigate } from "react-router-dom";
import ReactFlow, { Background, Handle, Position } from "reactflow";
import "reactflow/dist/style.css";

const CELL_WIDTH = 260;
const CELL_HEIGHT = 96;
const COL_GAP = 50;
const ROW_GAP = 70;

// Every chapter node shares one color — there's no per-lesson progress data
// yet to justify differentiating by depth, so availability is signaled with
// a small label instead. Only the subject node (added above the graph's own
// roots) keeps the amber brand accent, to set it apart as the graph's title.
const CHAPTER_COLOR = { bg: "#bb9974", text: "#18181a" };
const SUBJECT_COLOR = { bg: "var(--color-accent-amber-bg)", text: "var(--color-accent-amber-text)" };

function ChapterNode({ data }) {
  const colors = data.kind === "subject" ? SUBJECT_COLOR : CHAPTER_COLOR;
  return (
    <div
      style={{ background: colors.bg, width: CELL_WIDTH }}
      className={`rounded-xl px-4 py-3 border border-black/10 ${
        data.clickable ? "cursor-pointer hover:brightness-110" : "cursor-default"
      }`}
    >
      {data.kind !== "subject" && <Handle type="target" position={Position.Top} className="invisible" />}
      <div style={{ color: colors.text }} className="text-sm font-semibold leading-snug">
        {data.title}
      </div>
      {!data.available && data.kind !== "subject" && (
        <div style={{ color: colors.text }} className="text-xs opacity-70 mt-1">
          Bientôt disponible
        </div>
      )}
      <div className="h-1.5 w-full rounded-full bg-black/25 overflow-hidden mt-2">
        <div style={{ background: colors.text, width: "100%" }} className="h-full" />
      </div>
      <Handle type="source" position={Position.Bottom} className="invisible" />
    </div>
  );
}

const NODE_TYPES = { chapterNode: ChapterNode };

function findDocument(documents, matchSubstring) {
  if (!matchSubstring) return null;
  const needle = matchSubstring.toLowerCase();
  return documents.find((d) => d.title.toLowerCase().includes(needle)) ?? null;
}

export default function ChapterGraphView({ graph, documents }) {
  const navigate = useNavigate();

  const { nodes, edges } = useMemo(() => {
    const nodeById = Object.fromEntries(graph.nodes.map((n) => [n.id, n]));

    if (import.meta.env.DEV) {
      for (const node of graph.nodes) {
        for (const parentId of node.parents ?? []) {
          const parent = nodeById[parentId];
          if (parent.row >= node.row) {
            console.warn(
              `[ChapterGraphView] "${graph.title}": "${node.id}" (row ${node.row}) should be ` +
                `strictly below its parent "${parentId}" (row ${parent.row}).`
            );
          }
        }
      }
    }

    const rootIds = graph.nodes.filter((n) => n.root).map((n) => n.id);
    const rootCols = rootIds.map((id) => nodeById[id].col);
    const subjectCol = (Math.min(...rootCols) + Math.max(...rootCols)) / 2;

    const subjectNode = {
      id: "__subject__",
      type: "chapterNode",
      position: { x: subjectCol * (CELL_WIDTH + COL_GAP), y: -1 * (CELL_HEIGHT + ROW_GAP) },
      data: { title: graph.title, kind: "subject", clickable: false, available: true },
    };

    const chapterNodes = graph.nodes.map((node) => {
      const doc = findDocument(documents, node.match);
      const available = Boolean(doc && doc.status === "ready");
      return {
        id: node.id,
        type: "chapterNode",
        position: {
          x: node.col * (CELL_WIDTH + COL_GAP),
          y: node.row * (CELL_HEIGHT + ROW_GAP),
        },
        data: {
          title: node.title,
          kind: "chapter",
          available,
          clickable: available,
          documentId: doc?.id ?? null,
        },
      };
    });

    const subjectEdges = rootIds.map((id) => ({
      id: `__subject__-${id}`,
      source: "__subject__",
      target: id,
      type: "smoothstep",
      style: { stroke: "var(--color-border-subtle)", strokeWidth: 2 },
    }));

    const chapterEdges = graph.nodes.flatMap((node) =>
      (node.parents ?? []).map((parentId) => ({
        id: `${parentId}-${node.id}`,
        source: parentId,
        target: node.id,
        type: "smoothstep",
        style: { stroke: "var(--color-border-subtle)", strokeWidth: 2 },
      }))
    );

    return {
      nodes: [subjectNode, ...chapterNodes],
      edges: [...subjectEdges, ...chapterEdges],
    };
  }, [graph, documents]);

  // Handled via ReactFlow's own onNodeClick rather than an onClick inside the
  // custom node component — a click on content nested inside a React Flow
  // node can get absorbed by its internal drag/selection event layer instead
  // of reaching a plain DOM onClick, which was exactly why ingested chapters
  // weren't navigating anywhere despite being marked clickable.
  function handleNodeClick(_event, node) {
    if (node.data.clickable && node.data.documentId) {
      navigate(`/chapter/${node.data.documentId}`);
    }
  }

  return (
    <div className="h-full w-full">
      <ReactFlow
        nodes={nodes}
        edges={edges}
        nodeTypes={NODE_TYPES}
        onNodeClick={handleNodeClick}
        nodesDraggable={false}
        nodesConnectable={false}
        elementsSelectable={false}
        panOnScroll
        zoomOnScroll={false}
        fitView
        fitViewOptions={{ padding: 0.15 }}
        proOptions={{ hideAttribution: false }}
        style={{ background: "var(--color-canvas)" }}
      >
        <Background color="rgba(255, 255, 255, 0.5)" gap={24} size={1} />
      </ReactFlow>
    </div>
  );
}
