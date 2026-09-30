import { Link, NavLink, useNavigate } from "react-router-dom";
import kernelLogo from "../../assets/kernel.png";
import { useAuth } from "../../context/AuthContext";

const NAV_LINKS = [{ label: "Chapitres", to: "/chapters" }];

export default function Navbar() {
  const { isAuthenticated, logout } = useAuth();
  const navigate = useNavigate();

  return (
    <nav className="flex-shrink-0 flex items-center justify-between h-14 px-6 border-b border-neutral-800">
      <div className="flex items-center gap-x-8">
        <Link to="/" className="flex items-center gap-x-2">
          <img src={kernelLogo} alt="" className="h-7 w-7 object-contain" />
          <span className="font-semibold tracking-tight">Kernel</span>
        </Link>

        <div className="flex items-center gap-x-6">
          {NAV_LINKS.map((link) => (
            <NavLink
              key={link.to}
              to={link.to}
              className={({ isActive }) =>
                `text-sm ${isActive ? "text-white" : "text-neutral-400 hover:text-neutral-200"}`
              }
            >
              {link.label}
            </NavLink>
          ))}
        </div>
      </div>

      <div className="flex items-center gap-x-4">
        {isAuthenticated ? (
          <button
            onClick={() => { logout(); navigate("/"); }}
            className="text-sm px-3 py-1.5 rounded-md border border-neutral-700 text-neutral-300 hover:border-neutral-500 hover:text-white transition-colors"
          >
            Déconnexion
          </button>
        ) : (
          <Link
            to="/login"
            className="text-sm px-3 py-1.5 rounded-md border border-neutral-700 text-neutral-300 hover:border-neutral-500 hover:text-white transition-colors"
          >
            Connexion
          </Link>
        )}
      </div>
    </nav>
  );
}
