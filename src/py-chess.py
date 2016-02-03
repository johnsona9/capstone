import chess
import numpy as np
board = chess.Board()
move = chess.Move(chess.SQUARE_NAMES.index("e2"), chess.SQUARE_NAMES.index("e4"))
if move in board.legal_moves:
	board.push(chess.Move(chess.SQUARE_NAMES.index("e2"), chess.SQUARE_NAMES.index("e4")))
print board
print len(board.attackers(chess.WHITE, chess.D5))
board.push(chess.Move(chess.SQUARE_NAMES.index("e7"), chess.SQUARE_NAMES.index("e5")))
board.push(chess.Move(chess.SQUARE_NAMES.index("f1"), chess.SQUARE_NAMES.index("c4")))
print board
print len(board.attackers(chess.WHITE, chess.D5))
