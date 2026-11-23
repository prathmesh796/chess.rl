// app/api/selfplay/route.ts

import { NextRequest, NextResponse } from "next/server"
import prisma from "@/lib/prisma"

export async function POST(req: NextRequest) {
  const body = await req.json()

  const { type, payload } = body

  if (type === "create_game") {
    const result = payload.result === "1-0" ? "win" : payload.result === "0-1" ? "loss" : "draw"

    const game = await prisma.game.create({
      data: {
        result: result,
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

  if (type === "insert_bulk_move") {
    await prisma.move.createMany({
      data: payload,
    })

    return NextResponse.json({ success: true })
  }

  return NextResponse.json({ error: "Invalid type" })
}