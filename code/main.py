from king import king
from board import board
from knight import knight
from pawn import pawn
from bishop import bishop
from rook import rook

board = board()
king = king([1,1], "white", board)
knight = knight([1,1], "black", board)
pawn = pawn([2,2], "white", board)
bishop = bishop([3,3], "white", board)
rook = rook([2,6], "black", board)
board.placePiece([2,2], pawn)
board.placePiece([6,6], knight)

