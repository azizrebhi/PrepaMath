import { useEffect, useRef, useState } from "react";
import { Link, NavLink, useLocation, useNavigate } from "react-router-dom";
import { LogOut, User as UserIcon } from "lucide-react";
import kernelLogo from "../../assets/kernel.png";
import { useAuth } from "../../context/AuthContext";

const NAV_LINKS = [{ label: "Chapitres", to: "/chapters" }];

export default function Navbar() {
  const { isAuthenticated, user, logout } = useAuth();
  const navigate = useNavigate();
  const { pathname } = useLocation();
  const isLandingPage = pathname === "/";
  const [menuOpen, setMenuOpen] = useState(false);
  const menuRef = useRef(null);

  useEffect(() => {
    if (!menuOpen) return;
    function handleClickOutside(e) {
      if (menuRef.current && !menuRef.current.contains(e.target)) {
        setMenuOpen(false);
      }
    }
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, [menuOpen]);

  return (
    <div className={isLandingPage ? "flex-shrink-0 flex justify-center pt-4 px-4" : "flex-shrink-0"}>
      <nav
        className={
          isLandingPage
            ? "flex items-center justify-between h-14 px-6 w-full max-w-4xl rounded-full border border-neutral-800 bg-neutral-900/80 backdrop-blur"
            : "w-full flex items-center justify-between h-14 px-6 border-b border-neutral-800"
        }
      >
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
          <div className="relative" ref={menuRef}>
            <button
              onClick={() => setMenuOpen((v) => !v)}
              className="block h-8 w-8 rounded-full overflow-hidden border border-neutral-700 hover:border-neutral-500 transition-colors"
              aria-label="Compte"
            >
              {user?.picture ? (
                <img
                  src={user.picture}
                  alt=""
                  referrerPolicy="no-referrer"
                  className="h-full w-full object-cover"
                />
              ) : (
                <div className="h-full w-full flex items-center justify-center bg-neutral-800 text-neutral-400">
                  <UserIcon size={16} />
                </div>
              )}
            </button>

            {menuOpen && (
              <div className="absolute right-0 mt-2 w-48 rounded-md border border-neutral-800 bg-neutral-900 shadow-lg py-1 z-50">
                {user?.email && (
                  <div className="px-3 py-2 text-xs text-neutral-500 truncate border-b border-neutral-800">
                    {user.email}
                  </div>
                )}
                <button
                  onClick={() => {
                    setMenuOpen(false);
                    logout();
                    navigate("/");
                  }}
                  className="w-full flex items-center gap-2 px-3 py-2 text-sm text-neutral-300 hover:bg-neutral-800 hover:text-white transition-colors"
                >
                  <LogOut size={14} />
                  Déconnexion
                </button>
              </div>
            )}
          </div>
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
    </div>
  );
}
