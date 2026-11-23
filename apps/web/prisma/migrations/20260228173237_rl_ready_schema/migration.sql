-- CreateEnum
CREATE TYPE "Player" AS ENUM ('white', 'black');

-- CreateEnum
CREATE TYPE "Result" AS ENUM ('win', 'loss', 'draw');

-- CreateEnum
CREATE TYPE "GameStatus" AS ENUM ('fresh', 'completed', 'archived', 'bad');

-- CreateTable
CREATE TABLE "Game" (
    "id" TEXT NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "result" "Result" NOT NULL,
    "pgn" TEXT NOT NULL,
    "modelVersion" TEXT NOT NULL,
    "status" "GameStatus" NOT NULL DEFAULT 'fresh',

    CONSTRAINT "Game_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Move" (
    "id" TEXT NOT NULL,
    "gameId" TEXT NOT NULL,
    "moveIndex" INTEGER NOT NULL,
    "fen" TEXT NOT NULL,
    "moveUci" TEXT NOT NULL,
    "player" "Player" NOT NULL,
    "reward" DOUBLE PRECISION,

    CONSTRAINT "Move_pkey" PRIMARY KEY ("id")
);

-- AddForeignKey
ALTER TABLE "Move" ADD CONSTRAINT "Move_gameId_fkey" FOREIGN KEY ("gameId") REFERENCES "Game"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
