from king import king
from board import board
from knight import knight
from pawn import pawn
from bishop import bishop

board = board()
king = king([1,1], "white", board)
knight = knight([1,1], "black", board)
pawn = pawn([2,2], "white", board)
bishop = bishop([3,3], "white", board)
#board.placePiece([1,1], king)
board.placePiece([2,2], pawn)
board.placePiece([6,6], knight)
print bishop.attackedSquares()
# king.attackedSquares()
# knight.attackedSquares()
# pawn.attackedSquares()
