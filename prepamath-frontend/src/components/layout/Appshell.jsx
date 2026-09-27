import { Outlet } from "react-router-dom";
import Navbar from "./Navbar";

export default function AppShell() {
  return (
    <div className="flex flex-col h-screen bg-neutral-950 text-neutral-100">
      <Navbar />
      <main className="flex-1 overflow-hidden">
        <Outlet />
      </main>
    </div>
  );
}