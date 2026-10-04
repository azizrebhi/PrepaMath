import { createContext, useContext, useState, useEffect, useCallback } from "react";
import { useNavigate } from "react-router-dom";

const AuthContext = createContext(null);
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

export function AuthProvider({ children }) {
  const [token, setToken] = useState(() => localStorage.getItem("access_token"));
  const [user, setUser] = useState(null);

  useEffect(() => {
    if (token) {
      localStorage.setItem("access_token", token);
    } else {
      localStorage.removeItem("access_token");
    }
  }, [token]);

  // Not routed through useApiFetch — that hook depends on useAuth(), which
  // depends on this exact provider already being mounted, so it can't be
  // called from inside itself. A plain fetch is fine here: on failure we
  // just leave the profile unset rather than forcing a logout, since the
  // normal 401 handling elsewhere will catch genuine token expiry anyway.
  useEffect(() => {
    if (!token) {
      setUser(null);
      return;
    }
    let cancelled = false;
    fetch(`${API_BASE_URL}/users/me`, { headers: { Authorization: `Bearer ${token}` } })
      .then((res) => (res.ok ? res.json() : null))
      .then((data) => {
        if (!cancelled) setUser(data);
      })
      .catch(() => {
        if (!cancelled) setUser(null);
      });
    return () => {
      cancelled = true;
    };
  }, [token]);

  const value = {
    token,
    user,
    isAuthenticated: !!token,
    login: (newToken) => setToken(newToken),
    logout: () => setToken(null),
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

export function useAuth() {
  return useContext(AuthContext);
}

// Every authenticated request should go through this instead of raw fetch —
// it attaches the token automatically, and on a 401 (the token's eventually
// going to expire no matter how long its lifetime is) it clears the stale
// token and sends the user back to /login with a clear reason, instead of
// leaving a raw "401" error sitting on whatever page they happened to be on.
export function useApiFetch() {
  const { token, logout } = useAuth();
  const navigate = useNavigate();

  return useCallback(
    async (url, options = {}) => {
      const res = await fetch(url, {
        ...options,
        headers: {
          ...(options.headers || {}),
          Authorization: `Bearer ${token}`,
        },
      });

      if (res.status === 401) {
        logout();
        navigate("/login", { state: { sessionExpired: true }, replace: true });
        throw new Error("Session expirée — veuillez vous reconnecter.");
      }

      return res;
    },
    [token, logout, navigate]
  );
}
