import { Navigate, useLocation } from "react-router-dom";
import { useAuth } from "../../context/AuthContext";

// Guards a route at render time instead of waiting on a data fetch's 401 —
// without this, a logged-out visitor sees the full page (graph, workspace
// chrome) before any auth-required request even resolves.
export default function ProtectedRoute({ children }) {
  const { isAuthenticated } = useAuth();
  const location = useLocation();

  if (!isAuthenticated) {
    // Google OAuth leaves the page entirely (window.location.href to
    // google.com and back), which wipes router state — sessionStorage
    // survives that round trip, so GoogleCallbackPage can still read the
    // intended destination back out after the redirect returns.
    try {
      sessionStorage.setItem("post_login_redirect", location.pathname);
    } catch {
      // Private browsing / blocked storage — falls back to /chapters.
    }
    return <Navigate to="/login" state={{ from: location }} replace />;
  }

  return children;
}
