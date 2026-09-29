import { Routes, Route } from "react-router-dom";
import AppShell from "./components/layout/AppShell";
import WelcomePage from "./pages/WelcomePage";
import RoadmapPage from "./pages/RoadmapPage";
import ChapterWorkspacePage from "./pages/ChapterWorkspacePage";

export default function App() {
  return (
    <Routes>
      <Route element={<AppShell />}>
        <Route path="/" element={<WelcomePage />} />
        <Route path="/chapters" element={<RoadmapPage />} />
        <Route path="/chapter/:chapterId" element={<ChapterWorkspacePage />} />
      </Route>
    </Routes>
  );
}
