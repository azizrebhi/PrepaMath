import { Navigate, useLocation } from "react-router-dom";
import { useAuth } from "../../context/AuthContext";

// Guards a route at render time instead of waiting on a data fetch's 401 —
// without this, a logged-out visitor sees the full page (graph, workspace
// chrome) before any auth-required request even resolves.
export default function ProtectedRoute({ children }) {
  const { isAuthenticated } = useAuth();
  const location = useLocation();

  if (!isAuthenticated) {
    return <Navigate to="/login" state={{ from: location }} replace />;
  }

  return children;
}
