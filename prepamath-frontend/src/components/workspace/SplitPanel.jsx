import { useCallback, useEffect, useRef, useState } from "react";
import LeftPanel from "./LeftPanel";
import RightPanel from "./RightPanel";

const MIN_LEFT_PERCENT = 20;
const MAX_LEFT_PERCENT = 70;

export default function SplitPanel() {
  const containerRef = useRef(null);
  const [leftWidth, setLeftWidth] = useState(40); // percent
  const [isDragging, setIsDragging] = useState(false);
  const [selectedPartId, setSelectedPartId] = useState(null);
  const [currentLessonChunkIds, setCurrentLessonChunkIds] = useState([]);

  const handleMouseDown = useCallback((e) => {
    e.preventDefault(); // stops text-selection while dragging
    setIsDragging(true);
  }, []);

  useEffect(() => {
    if (!isDragging) return;

    function handleMouseMove(e) {
      const rect = containerRef.current.getBoundingClientRect();
      const rawPercent = ((e.clientX - rect.left) / rect.width) * 100;
      const clamped = Math.min(MAX_LEFT_PERCENT, Math.max(MIN_LEFT_PERCENT, rawPercent));
      setLeftWidth(clamped);
    }

    function handleMouseUp() {
      setIsDragging(false);
    }

    window.addEventListener("mousemove", handleMouseMove);
    window.addEventListener("mouseup", handleMouseUp);

    return () => {
      window.removeEventListener("mousemove", handleMouseMove);
      window.removeEventListener("mouseup", handleMouseUp);
    };
  }, [isDragging]);

  return (
    <div
      ref={containerRef}
      className={`flex h-full gap-1 p-2 bg-canvas ${isDragging ? "select-none" : ""}`}
    >
      <div
        style={{ width: `${leftWidth}%` }}
        className="bg-surface border border-border-subtle rounded-lg overflow-y-auto"
      >
        <LeftPanel
          selectedPartId={selectedPartId}
          setSelectedPartId={setSelectedPartId}
          setCurrentLessonChunkIds={setCurrentLessonChunkIds}
        />
      </div>

      <div
        onMouseDown={handleMouseDown}
        className="w-3 flex-shrink-0 flex items-center justify-center cursor-col-resize group"
      >
        <div className="h-10 w-1 rounded-full bg-border-subtle group-hover:bg-ink-muted transition-colors" />
      </div>

      <div className="flex-1 bg-surface border border-border-subtle rounded-lg overflow-hidden">
        <RightPanel selectedPartId={selectedPartId} currentLessonChunkIds={currentLessonChunkIds} />
      </div>
    </div>
  );
}
