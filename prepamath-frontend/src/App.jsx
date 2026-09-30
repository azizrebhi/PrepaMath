import { Routes, Route } from "react-router-dom";
import AppShell from "./components/layout/AppShell";
import WelcomePage from "./pages/WelcomePage";
import RoadmapPage from "./pages/RoadmapPage";
import ChapterWorkspacePage from "./pages/ChapterWorkspacePage";
import LoginPage from "./pages/LoginPage";
import RegisterPage from "./pages/RegisterPage";
import GoogleCallbackPage from "./pages/GoogleCallbackPage";

export default function App() {
  return (
    <Routes>
      <Route element={<AppShell />}>
        <Route path="/" element={<WelcomePage />} />
        <Route path="/chapters" element={<RoadmapPage />} />
        <Route path="/chapter/:chapterId" element={<ChapterWorkspacePage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegisterPage />} />
        <Route path="/auth/google/callback" element={<GoogleCallbackPage />} />
      </Route>
    </Routes>
  );
}
