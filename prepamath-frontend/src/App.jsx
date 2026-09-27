import { Routes, Route } from "react-router-dom";
import AppShell from "./components/layout/AppShell";
import RoadmapPage from "./pages/RoadmapPage";
import ChapterWorkspacePage from "./pages/ChapterWorkspacePage";

export default function App() {
  return (
    <Routes>
      <Route element={<AppShell />}>
        <Route path="/" element={<RoadmapPage />} />
        <Route path="/chapter/:chapterId" element={<ChapterWorkspacePage />} />
        {/* TODO 0: RoadmapPage and ChapterWorkspacePage don't exist yet.
            Create both under src/pages/ as a bare-minimum placeholder first,
            e.g.:
              export default function RoadmapPage() {
                return <div>Roadmap page</div>;
              }
            Get the route rendering that before building real content. */}
      </Route>
    </Routes>
  );
}