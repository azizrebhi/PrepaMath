import { Link } from "react-router-dom";
import kernelLogo from "../assets/kernel.png";

export default function WelcomePage() {
  return (
    <div className="h-full overflow-y-auto">
      <div className="max-w-6xl mx-auto px-6 py-20 flex flex-col md:flex-row items-center gap-16">
        <div className="flex-1 max-w-xl">
          <h1 className="text-5xl md:text-6xl font-bold tracking-tight leading-[1.05]">
            Une meilleure façon de
            <br />
            <span className="text-violet-400">réviser tes maths de prépa.</span>
          </h1>

          <p className="mt-6 text-neutral-400 text-lg leading-relaxed">
            Des explications générées par IA, fondées sur ton propre cours —
            de l'algèbre linéaire à la topologie, pensé pour les classes
            préparatoires.
          </p>

          <Link
            to="/chapters"
            className="inline-block mt-8 px-6 py-3 rounded-lg bg-violet-600 hover:bg-violet-500 text-white font-medium transition-colors"
          >
            Voir les chapitres
          </Link>
        </div>

        <div className="flex-1 flex items-center justify-center">
          <div className="relative">
            <div className="absolute inset-0 bg-violet-600/30 blur-3xl rounded-full" />
            <img
              src={kernelLogo}
              alt="Kernel"
              className="relative w-64 h-64 md:w-80 md:h-80 object-contain"
            />
          </div>
        </div>
      </div>
    </div>
  );
}
