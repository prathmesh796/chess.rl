import { NextResponse } from "next/server"
import prisma from "@/lib/prisma"

export async function GET() {
  const data = await prisma.move.findMany({
    where: {
      reward: { not: null },
    },
    select: {
      fen: true,
      reward: true,
      moveIndex: true,
    },
    take: 20000,
  })

  return NextResponse.json(data)
}