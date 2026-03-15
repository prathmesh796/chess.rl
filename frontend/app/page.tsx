"use client";

import { useRouter } from "next/navigation";
import { motion } from "framer-motion";
import { Play, BrainCircuit, Activity, ChevronRight, Award } from "lucide-react";

export default function Home() {
  const router = useRouter();

  return (
    <div className="relative min-h-screen bg-slate-950 text-white overflow-hidden selection:bg-indigo-500/30 font-sans">
      {/* Dynamic Background */}
      <div className="absolute inset-0 z-0">
        <div className="absolute top-[-20%] left-[-10%] w-[50%] h-[50%] rounded-full bg-indigo-600/20 blur-[120px]" />
        <div className="absolute bottom-[-20%] right-[-10%] w-[50%] h-[50%] rounded-full bg-blue-600/20 blur-[120px]" />
        <div className="absolute top-[40%] left-[60%] w-[30%] h-[30%] rounded-full bg-purple-600/20 blur-[100px]" />
      </div>

      <div className="relative z-10 container mx-auto px-6 pt-32 pb-24 flex flex-col items-center justify-center min-h-screen">

        {/* Badge */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
          className="flex items-center gap-2 px-4 py-2 rounded-full bg-indigo-500/10 border border-indigo-500/20 text-indigo-300 font-medium text-sm mb-8 backdrop-blur-md"
        >
          <BrainCircuit className="w-4 h-4" />
          <span>Powered by Deep Neural Networks</span>
        </motion.div>

        {/* Hero Headline */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5, delay: 0.1 }}
          className="text-center max-w-4xl"
        >
          <h1 className="text-6xl md:text-8xl font-extrabold tracking-tight mb-8">
            Challenge the <br />
            <span className="text-transparent bg-clip-text bg-linear-to-r from-indigo-400 via-blue-400 to-purple-400 drop-shadow-sm">
              Intelligence
            </span>
          </h1>
          <p className="text-xl md:text-2xl text-slate-400 mb-12 max-w-2xl mx-auto leading-relaxed">
            Experience next-generation chess gameplay. Play against an advanced AI model that learns and adapts to your strategy in real-time.
          </p>
        </motion.div>

        {/* Action Buttons */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5, delay: 0.2 }}
          className="flex flex-col sm:flex-row items-center gap-6"
        >
          <button
            onClick={() => router.push("/play")}
            className="group relative inline-flex items-center justify-center gap-3 px-8 py-4 bg-white text-slate-950 font-bold text-lg rounded-full hover:scale-105 active:scale-95 transition-all shadow-[0_0_40px_rgba(255,255,255,0.3)] hover:shadow-[0_0_60px_rgba(255,255,255,0.5)]"
          >
            <Play className="w-5 h-5 fill-slate-950" />
            <span>Play Now</span>
            <ChevronRight className="w-5 h-5 text-slate-600 group-hover:translate-x-1 transition-transform" />
          </button>

          <button
            onClick={() => router.push("/dashboard")}
            className="group relative inline-flex items-center justify-center gap-3 px-8 py-4 bg-slate-900 border border-slate-800 text-white font-semibold text-lg rounded-full hover:bg-slate-800 transition-all hover:border-slate-700"
          >
            <Activity className="w-5 h-5 text-indigo-400" />
            <span>View Stats</span>
          </button>
        </motion.div>

        {/* Features / Floating Cards */}
        <motion.div
          initial={{ opacity: 0, y: 40 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.7, delay: 0.4 }}
          className="mt-24 grid grid-cols-1 md:grid-cols-3 gap-6 max-w-5xl w-full"
        >
          {[
            {
              icon: <BrainCircuit className="w-6 h-6 text-blue-400" />,
              title: "Adaptive AI",
              desc: "The engine scales its complexity based on your Elo rating."
            },
            {
              icon: <Activity className="w-6 h-6 text-indigo-400" />,
              title: "Real-time Analytics",
              desc: "Get post-game insights into your blunders and brilliancies."
            },
            {
              icon: <Award className="w-6 h-6 text-purple-400" />,
              title: "Global Leaderboards",
              desc: "Compete against players worldwide and climb the ranks."
            }
          ].map((feature, i) => (
            <div key={i} className="p-6 rounded-2xl bg-white/3 border border-white/5 backdrop-blur-sm hover:bg-white/5 transition-colors group">
              <div className="w-12 h-12 rounded-xl bg-white/5 flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
                {feature.icon}
              </div>
              <h3 className="text-xl font-semibold mb-2 text-white/90">{feature.title}</h3>
              <p className="text-slate-400 leading-relaxed">{feature.desc}</p>
            </div>
          ))}
        </motion.div>
      </div>
    </div>
  );
}
