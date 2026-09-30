import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

export default function RegisterPage() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);
  const { login } = useAuth();
  const navigate = useNavigate();

  async function handleSubmit(e) {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      const registerRes = await fetch(`${API_BASE_URL}/auth/register`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
      });
      if (!registerRes.ok) {
        const data = await registerRes.json().catch(() => null);
        throw new Error(data?.detail?.reason || data?.detail || "Impossible de créer le compte.");
      }

      const body = new URLSearchParams();
      body.set("username", email);
      body.set("password", password);
      const loginRes = await fetch(`${API_BASE_URL}/auth/jwt/login`, {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body,
      });
      const loginData = await loginRes.json();
      login(loginData.access_token);
      navigate("/chapters");
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="h-full flex items-center justify-center">
      <div className="w-full max-w-sm p-8 rounded-lg border border-neutral-800 bg-neutral-900">
        <h1 className="text-2xl font-semibold text-center">Créer un compte</h1>

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
              minLength={8}
              className="w-full bg-neutral-950 border border-neutral-800 rounded-md p-2 text-sm outline-none focus:border-violet-500"
            />
          </div>

          {error && <p className="text-sm text-red-400">{error}</p>}

          <button
            type="submit"
            disabled={loading}
            className="w-full py-2 rounded-md bg-violet-600 hover:bg-violet-500 disabled:opacity-50 font-medium transition-colors"
          >
            {loading ? "Création..." : "Créer mon compte"}
          </button>
        </form>

        <div className="my-6 flex items-center gap-3">
          <div className="flex-1 h-px bg-neutral-800" />
          <span className="text-xs text-neutral-500">ou</span>
          <div className="flex-1 h-px bg-neutral-800" />
        </div>

        <button
          onClick={async () => {
            const res = await fetch(`${API_BASE_URL}/auth/google/authorize`, {
              credentials: "include",
            });
            const data = await res.json();
            window.location.href = data.authorization_url;
          }}
          className="w-full py-2 rounded-md border border-neutral-700 hover:border-neutral-500 text-sm transition-colors"
        >
          Continuer avec Google
        </button>

        <p className="mt-6 text-sm text-neutral-500 text-center">
          Déjà un compte ?{" "}
          <Link to="/login" className="text-violet-400 hover:underline">
            Se connecter
          </Link>
        </p>
      </div>
    </div>
  );
}
