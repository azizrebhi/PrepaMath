import { useState } from "react";
import { Link, useLocation, useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

export default function LoginPage() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);
  const { login } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();
  const sessionExpired = location.state?.sessionExpired;
  const redirectTo = location.state?.from?.pathname ?? "/chapters";

  async function handleSubmit(e) {
    e.preventDefault();
    setLoading(true);
    setError(null);

    const body = new URLSearchParams();
    body.set("username", email);
    body.set("password", password);

    try {
      const res = await fetch(`${API_BASE_URL}/auth/jwt/login`, {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body,
      });
      if (!res.ok) throw new Error("Email ou mot de passe incorrect.");
      const data = await res.json();
      login(data.access_token);
      navigate(redirectTo, { replace: true });
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }

  async function handleGoogleLogin() {
    const res = await fetch(`${API_BASE_URL}/auth/google/authorize`, {
      credentials: "include",
    });
    const data = await res.json();
    window.location.href = data.authorization_url;
  }

  return (
    <div className="h-full flex items-center justify-center">
      <div className="w-full max-w-sm p-8 rounded-lg border border-neutral-800 bg-neutral-900">
        <h1 className="text-2xl font-semibold text-center">Connexion</h1>

        {sessionExpired && (
          <p className="mt-4 text-sm text-amber-400 bg-amber-950/40 border border-amber-900 rounded-md px-3 py-2">
            Votre session a expiré — veuillez vous reconnecter.
          </p>
        )}

        <form onSubmit={handleSubmit} className="mt-6 space-y-4">
          <div>
            <label className="block text-sm text-neutral-400 mb-1">Email</label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
              className="w-full bg-neutral-950 border border-neutral-800 rounded-md p-2 text-sm outline-none focus:border-violet-500"
            />
          </div>

          <div>
            <label className="block text-sm text-neutral-400 mb-1">Mot de passe</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
              className="w-full bg-neutral-950 border border-neutral-800 rounded-md p-2 text-sm outline-none focus:border-violet-500"
            />
          </div>

          {error && <p className="text-sm text-red-400">{error}</p>}

          <button
            type="submit"
            disabled={loading}
            className="w-full py-2 rounded-md bg-violet-600 hover:bg-violet-500 disabled:opacity-50 font-medium transition-colors"
          >
            {loading ? "Connexion..." : "Se connecter"}
          </button>
        </form>

        <div className="my-6 flex items-center gap-3">
          <div className="flex-1 h-px bg-neutral-800" />
          <span className="text-xs text-neutral-500">ou</span>
          <div className="flex-1 h-px bg-neutral-800" />
        </div>

        <button
          onClick={handleGoogleLogin}
          className="w-full py-2 rounded-md border border-neutral-700 hover:border-neutral-500 text-sm transition-colors"
        >
          Continuer avec Google
        </button>

        <p className="mt-6 text-sm text-neutral-500 text-center">
          Pas encore de compte ?{" "}
          <Link to="/register" className="text-violet-400 hover:underline">
            Créer un compte
          </Link>
        </p>
      </div>
    </div>
  );
}
