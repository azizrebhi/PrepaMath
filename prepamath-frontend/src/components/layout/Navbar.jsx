import { NavLink } from "react-router-dom";

// TODO 1: your actual nav destinations, as { label, to } objects.
// Leave it empty and the navbar will just render logo + right side —
// that's a valid way to confirm the layout works before adding content.
const NAV_LINKS = [
  // { label: "Chapters", to: "/" },
];

export default function Navbar() {
  return (
    <nav className="flex-shrink-0 flex items-center justify-between h-14 px-6 border-b border-neutral-800">
      <div className="flex items-center gap-x-8">
        {/* TODO 2: your logo/icon + app name, replacing this span */}
        <span className="font-semibold">{/* app name */}</span>

        <div className="flex items-center gap-x-6">
          {NAV_LINKS.map((link) => (
            <NavLink
              key={link.to}
              to={link.to}
              // TODO 3: style the active link differently using the
              // `isActive` flag NavLink gives this callback for free.
              // Return a string of Tailwind classes, e.g.:
              //   isActive ? "text-white" : "text-neutral-400 hover:text-neutral-200"
              className={({ isActive }) => undefined}
            >
              {link.label}
            </NavLink>
          ))}
        </div>
      </div>

      <div className="flex items-center gap-x-4">
        {/* TODO 4: right-side icons/avatar. No auth yet, so just a static
            placeholder for now, e.g.:
              <div className="w-8 h-8 rounded-full bg-neutral-700" /> */}
      </div>
    </nav>
  );
}
