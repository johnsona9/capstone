from pawn import pawn
from rook import rook
from knight import knight
from bishop import bishop
from queen import queen
from king import king
from board import board
from game import game


board = board()
game = game(board)
print board.printBoard()
board.getPiece([2,2]).movePiece([3,2])
print board.printBoard()
