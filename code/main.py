from piece import piece
from pawn import pawn
from rook import rook
from knight import knight
from bishop import bishop
from queen import queen
from king import king
from board import board
from game import game
import lighter

squareDictionary = {'a1': [1,1], 'a2': [2,1], 'a3': [3,1], 'a4': [4,1], 'a5': [5,1], 'a6': [6,1], 'a7': [7,1], 'a8': [8,1], 
                    'b1': [1,2], 'b2': [2,2], 'b3': [3,2], 'b4': [4,2], 'b5': [5,2], 'b6': [6,2], 'b7': [7,2], 'b8': [8,2],
                    'c1': [1,3], 'c2': [2,3], 'c3': [3,3], 'c4': [4,3], 'c5': [5,3], 'c6': [6,3], 'c7': [7,3], 'c8': [8,3],
                    'd1': [1,4], 'd2': [2,4], 'd3': [3,4], 'd4': [4,4], 'd5': [5,4], 'd6': [6,4], 'd7': [7,4], 'd8': [8,4],
                    'e1': [1,5], 'e2': [2,5], 'e3': [3,5], 'e4': [4,5], 'e5': [5,5], 'e6': [6,5], 'e7': [7,5], 'e8': [8,5],
                    'f1': [1,6], 'f2': [2,6], 'f3': [3,6], 'f4': [4,6], 'f5': [5,6], 'f6': [6,6], 'f7': [7,6], 'f8': [8,6],
                    'g1': [1,7], 'g2': [2,7], 'g3': [3,7], 'g4': [4,7], 'g5': [5,7], 'g6': [6,7], 'g7': [7,7], 'g8': [8,7],
                    'h1': [1,8], 'h2': [2,8], 'h3': [3,8], 'h4': [4,8], 'h5': [5,8], 'h6': [6,8], 'h7': [7,8], 'h8': [8,8]}
board = board()
game = game(board)

def requestFirst(prompt):
    value = raw_input(prompt)
    if isinstance(board.getPiece(squareDictionary[value]), piece):
        return value
    else:
        print "There is no piece on that square, please pick another square."
        return request(prompt)

for e in reversed(board.printBoard()):
    print e
while 1:
    fromSquare = squareDictionary[requestFirst("Piece moving from square: ")]
    toSquare = squareDictionary[raw_input("Piece moves to square: ")]
    board.getPiece(fromSquare).movePiece(toSquare)
    lighter(board.getAttacked())
    for e in reversed(board.printBoard()):
        print e
    for e in reversed(board.getAttacked()):
        print e
