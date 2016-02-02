import chess
import numpy as np
board = chess.Board()
move = chess.Move(chess.SQUARE_NAMES.index("e2"), chess.SQUARE_NAMES.index("e4"))
if move in board.legal_moves:
	board.push(chess.Move(chess.SQUARE_NAMES.index("e2"), chess.SQUARE_NAMES.index("e4")))
print board
print board.legal_moves
print move
