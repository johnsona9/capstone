from king import king
from board import board
from knight import knight
from pawn import pawn
board = board()


king = king([1,1], "white", board)
knight = knight([1,1], "black", board)
pawn = pawn([2,2], "white", board)

board.placePiece([1,1], king)
board.placePiece([2,2], pawn)

king.attackedSquares()
knight.attackedSquares()
pawn.attackedSquares()
print board.isFull([1,1])
print board.isFull([2,2])