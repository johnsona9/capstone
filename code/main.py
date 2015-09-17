from king import king
from board import board
from knight import knight
from pawn import pawn

king = king([1,1], "white", board())
knight = knight([1,1], "black", board())
pawn = pawn([2,2], "white", board())
king.attackedSquares()
knight.attackedSquares()
pawn.attackedSquares()