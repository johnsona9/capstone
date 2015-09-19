from king import king
from board import board
from knight import knight
from pawn import pawn
from bishop import bishop
from rook import rook
from queen import queen

board = board()
king = king([1,1], "white", board)
knight = knight([1,1], "black", board)
pawn = pawn([2,2], "white", board)
bishop = bishop([2,4], "white", board)
rook = rook([2,6], "black", board)
queen = queen([2,4], "white", board)
board.placePiece([2,2], pawn)
board.placePiece([5,7], knight)
board.placePiece([2,6], rook)
print queen.attackedSquares()

