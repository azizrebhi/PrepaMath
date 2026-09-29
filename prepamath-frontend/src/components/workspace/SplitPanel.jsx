import { useCallback, useEffect, useRef, useState } from "react";
import LeftPanel from "./LeftPanel";
import RightPanel from "./RightPanel";

const MIN_LEFT_PERCENT = 20;
const MAX_LEFT_PERCENT = 70;
const PANEL_COLOR = "#262527";

export default function SplitPanel() {
  const containerRef = useRef(null);
  const [leftWidth, setLeftWidth] = useState(40); // percent
  const [isDragging, setIsDragging] = useState(false);

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
      className={`flex h-full gap-1 p-2 ${isDragging ? "select-none" : ""}`}
    >
      <div
        style={{ width: `${leftWidth}%`, backgroundColor: PANEL_COLOR }}
        className="rounded-lg overflow-y-auto"
      >
        <LeftPanel />
      </div>

      <div
        onMouseDown={handleMouseDown}
        className="w-3 flex-shrink-0 flex items-center justify-center cursor-col-resize group"
      >
        <div className="h-10 w-1 rounded-full bg-neutral-700 group-hover:bg-neutral-500 transition-colors" />
      </div>

      <div
        style={{ backgroundColor: PANEL_COLOR }}
        className="flex-1 rounded-lg overflow-hidden"
      >
        <RightPanel />
      </div>
    </div>
  );
}
