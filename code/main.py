from pawn import pawn
from rook import rook
from knight import knight
from bishop import bishop
from queen import queen
from king import king
from board import board
from game import game

squareDictionary = {'a1': [1,1], 'a2': [1,2], 'a3': [1,3], 'a4': [1,4], 'a5': [1,5], 'a6': [1,6], 'a7': [1,7], 'a8': [1,8], 
                    'b1': [2,1], 'b2': [2,2], 'b3': [2,3], 'b4': [2,4], 'b5': [2,5], 'b6': [2,6], 'b7': [2,7], 'b8': [2,8],
                    'c1': [3,1], 'c2': [3,2], 'c3': [3,3], 'c4': [3,4], 'c5': [3,5], 'c6': [3,6], 'c7': [3,7], 'c8': [3,8],
                    'd1': [4,1], 'd2': [4,2], 'd3': [4,3], 'd4': [4,4], 'd5': [4,5], 'd6': [4,6], 'd7': [4,7], 'd8': [4,8],
                    'e1': [5,1], 'e2': [5,2], 'e3': [5,3], 'e4': [5,4], 'e5': [5,5], 'e6': [5,6], 'e7': [5,7], 'e8': [5,8],
                    'f1': [6,1], 'f2': [6,2], 'f3': [6,3], 'f4': [6,4], 'f5': [6,5], 'f6': [6,6], 'f7': [6,7], 'f8': [6,8],
                    'g1': [7,1], 'g2': [7,2], 'g3': [7,3], 'g4': [7,4], 'g5': [7,5], 'g6': [7,6], 'g7': [7,7], 'g8': [7,8],
                    'h1': [8,1], 'h2': [8,2], 'h3': [8,3], 'h4': [8,4], 'h5': [8,5], 'h6': [8,6], 'h7': [8,7], 'h8': [8,8]}
board = board()
game = game(board)

# board.getPiece([8,5]).movePiece([5,5])
# for e in reversed(board.getAttacked()):
#     print e
for e in reversed(board.printBoard()):
    print e


fromSquare = raw_input("Piece moves from square: ")
toSquare = raw_input("Piece moves to square: ")
print board.getPiece(squareDictionary[fromSquare]) 
print board.getPiece(squareDictionary[fromSquare]).color
print board.getPiece(squareDictionary[toSquare]) 
print board.getPiece(squareDictionary[toSquare]).color