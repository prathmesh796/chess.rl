"use client";

import dynamic from "next/dynamic";
import { ArrowLeft } from "lucide-react";
import { useRouter } from "next/navigation";

// Dynamically import the ChessBoardWrapper to avoid SSR issues
const ChessBoardWrapper = dynamic(() => import("./ChessBoardWrapper").then((mod) => ({ default: mod.ChessBoardWrapper })),
    {
        ssr: false,
        loading: () => (
            <div className="w-full max-w-[600px] aspect-square bg-slate-800/50 rounded-lg border border-slate-700 flex items-center justify-center backdrop-blur-sm animate-pulse">
                <span className="text-slate-400 font-medium">Initializing Engine...</span>
            </div>
        )
    }
);

export default function PlayPage() {
    const router = useRouter();

    return (
        <div className="min-h-screen bg-slate-950 text-slate-200 selection:bg-indigo-500/30">
            {/* Ambient Background */}
            <div className="fixed inset-0 z-0 pointer-events-none overflow-hidden">
                <div className="absolute top-0 right-[20%] w-[500px] h-[500px] rounded-full bg-indigo-900/20 blur-[150px]" />
                <div className="absolute bottom-[10%] left-[10%] w-[600px] h-[600px] rounded-full bg-purple-900/10 blur-[150px]" />
            </div>

            {/* Header */}
            <header className="relative z-10 border-b border-slate-800/60 bg-slate-950/50 backdrop-blur-lg">
                <div className="container mx-auto px-6 h-16 flex items-center justify-between">
                    <button
                        onClick={() => router.push("/")}
                        className="flex items-center gap-2 text-slate-400 hover:text-white transition-colors group"
                    >
                        <ArrowLeft className="w-4 h-4 group-hover:-translate-x-1 transition-transform" />
                        <span className="font-medium text-sm">Back Home</span>
                    </button>

                    <div className="flex items-center gap-3">
                        <div className="w-8 h-8 rounded-full bg-linear-to-r from-indigo-500 to-purple-500 flex items-center justify-center text-xs font-bold shadow-[0_0_15px_rgba(99,102,241,0.5)]">
                            AI
                        </div>
                        <span className="font-semibold tracking-wide">v0.1.0 Alpha</span>
                    </div>
                </div>
            </header>

            {/* Main Content */}
            <main className="relative z-10 container mx-auto px-4 py-8 md:py-12 flex flex-col lg:flex-row items-start justify-center gap-8 lg:gap-16">

                {/* Board Area */}
                <div className="w-full max-w-[640px] shrink-0 flex flex-col gap-4">
                    {/* Opponent Info */}
                    <div className="flex items-center gap-4 bg-slate-900/40 p-3 rounded-xl border border-slate-800 backdrop-blur-md">
                        <div className="w-12 h-12 rounded-lg bg-indigo-500/10 border border-indigo-500/30 flex items-center justify-center">
                            🤖
                        </div>
                        <div>
                            <h3 className="font-bold text-lg text-slate-100 leading-tight">Neural Engine</h3>
                            <p className="text-sm text-slate-400">Rating: Computing...</p>
                        </div>
                    </div>

                    {/* Chess Board */}
                    <div className="relative p-1 md:p-2 rounded-2xl bg-slate-800/50 border border-slate-700/50 shadow-2xl shadow-indigo-500/10 backdrop-blur-xl">
                        <ChessBoardWrapper initialFen="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w - - 0 1" />
                    </div>

                    {/* Player Info */}
                    <div className="flex items-center justify-between gap-4 bg-slate-900/40 p-3 rounded-xl border border-slate-800 backdrop-blur-md">
                        <div className="flex items-center gap-4">
                            <div className="w-12 h-12 rounded-lg bg-slate-800 border border-slate-700 flex items-center justify-center">
                                👤
                            </div>
                            <div>
                                <h3 className="font-bold text-lg text-slate-100 leading-tight">Guest Player</h3>
                                <p className="text-sm text-slate-400">White Pieces</p>
                            </div>
                        </div>
                    </div>
                </div>

                {/* Sidebar (Analysis / Game State) */}
                <aside className="w-full lg:w-[400px] flex flex-col gap-6">
                    <div className="bg-slate-900/40 border border-slate-800 rounded-2xl p-6 backdrop-blur-md">
                        <h2 className="text-xl font-bold mb-4 flex items-center gap-2">
                            <span className="w-2 h-2 rounded-full bg-green-500 animate-pulse shadow-[0_0_10px_rgba(34,197,94,0.5)]" />
                            Match Activity
                        </h2>

                        <div className="space-y-4">
                            <div className="p-4 rounded-xl bg-slate-800/50 border border-slate-700/50">
                                <p className="text-sm text-slate-400 mb-1">Status</p>
                                <p className="font-medium text-indigo-300">Your Turn</p>
                            </div>

                            <div className="p-4 rounded-xl bg-slate-800/50 border border-slate-700/50">
                                <p className="text-sm text-slate-400 mb-2">Engine Evaluation</p>
                                <div className="h-2 w-full bg-slate-700 rounded-full overflow-hidden flex">
                                    <div className="h-full bg-white w-1/2 rounded-l-full" />
                                    <div className="h-full bg-slate-900 w-1/2 rounded-r-full" />
                                </div>
                                <p className="text-xs text-center mt-2 text-slate-500">0.00 Equal</p>
                            </div>
                        </div>
                    </div>
                </aside>

            </main>
        </div>
    );
}