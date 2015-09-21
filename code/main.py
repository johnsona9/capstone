from king import king
from board import board
from knight import knight
from pawn import pawn
from bishop import bishop
from rook import rook
from queen import queen

board = board()
king = king([1,1], "white", board)
board.placePiece([1,1], king)
print board.getAttacked()