// app/api/selfplay/route.ts

import { NextRequest, NextResponse } from "next/server"
import prisma from "@/lib/prisma"

export async function POST(req: NextRequest) {
    console.log("url: ")
  const body = await req.json()

  const { type, payload } = body

  if (type === "create_game") {
    const game = await prisma.game.create({
      data: {
        result: "draw",
        pgn: "",
        modelVersion: payload.modelVersion,
        status: "fresh",
      },
    })

    return NextResponse.json({ gameId: game.id })
  }

  if (type === "insert_move") {
    await prisma.move.create({
      data: payload,
    })

    return NextResponse.json({ success: true })
  }

  if (type === "update_rewards") {
    const { gameId, winner } = payload

    const moves = await prisma.move.findMany({
      where: { gameId },
    })

    for (const move of moves) {
      await prisma.move.update({
        where: { id: move.id },
        data: {
          reward:
            winner === "draw"
              ? 0
              : move.player === winner
              ? 1
              : -1,
        },
      })
    }

    await prisma.game.update({
      where: { id: gameId },
      data: {
        result:
          winner === "white"
            ? "win"
            : winner === "black"
            ? "loss"
            : "draw",
        status: "completed",
      },
    })

    return NextResponse.json({ success: true })
  }

  return NextResponse.json({ error: "Invalid type" })
}