import { useEffect, useState, useRef } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

export default function GoogleCallbackPage() {
  const [error, setError] = useState(null);
  const { login } = useAuth();
  const navigate = useNavigate();
  const calledRef = useRef(false);

  useEffect(() => {
    if (calledRef.current) return;
    calledRef.current = true;

    async function completeLogin() {
      try {
        const res = await fetch(
          `${API_BASE_URL}/auth/google/callback${window.location.search}`,
          { credentials: "include" }
        );
        if (!res.ok) throw new Error("Échec de la connexion Google.");
        const data = await res.json();
        login(data.access_token);

        let redirectTo = "/chapters";
        try {
          redirectTo = sessionStorage.getItem("post_login_redirect") ?? "/chapters";
          sessionStorage.removeItem("post_login_redirect");
        } catch {
          // Private browsing / blocked storage — falls back to /chapters.
        }
        navigate(redirectTo, { replace: true });
      } catch (err) {
        setError(err.message);
      }
    }
    completeLogin();
  }, []);

  return (
    <div className="h-full flex items-center justify-center">
      {error ? (
        <p className="text-red-400 text-sm">{error}</p>
      ) : (
        <p className="text-neutral-400 text-sm">Connexion en cours...</p>
      )}
    </div>
  );
}
