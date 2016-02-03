from pawn import pawn
from rook import rook
from knight import knight
from bishop import bishop
from queen import queen
from king import king
from board import board

class game(object):
    
    def __init__(self, board):
        self.board = board
        self.initialPosition(self.board)
        
        
    def initialPosition(self, board):
        pieces = []
        pieces.append(pawn([2,1], "white", board))
        pieces.append(pawn([2,2], "white", board))
        pieces.append(pawn([2,3], "white", board))
        pieces.append(pawn([2,4], "white", board))
        pieces.append(pawn([2,5], "white", board))
        pieces.append(pawn([2,6], "white", board))
        pieces.append(pawn([2,7], "white", board))
        pieces.append(pawn([2,8], "white", board))
    
        pieces.append(rook([1,1], "white", board))
        pieces.append(rook([1,8], "white", board))
        pieces.append(knight([1,2], "white", board))
        pieces.append(knight([1,7], "white", board))
        pieces.append(bishop([1,3], "white", board))
        pieces.append(bishop([1,6], "white", board))
        pieces.append(king([1,5], "white", board))
        pieces.append(queen([1,4], "white", board))

        pieces.append(pawn([7,1], "black", board))
        pieces.append(pawn([7,2], "black", board))
        pieces.append(pawn([7,3], "black", board))
        pieces.append(pawn([7,4], "black", board))
        pieces.append(pawn([7,5], "black", board))
        pieces.append(pawn([7,6], "black", board))
        pieces.append(pawn([7,7], "black", board))
        pieces.append(pawn([7,8], "black", board))

        pieces.append(rook([8,1], "black", board))
        pieces.append(rook([8,8], "black", board))
        pieces.append(knight([8,2], "black", board))
        pieces.append(knight([8,7], "black", board))
        pieces.append(bishop([8,3], "black", board))
        pieces.append(bishop([8,6], "black", board))
        pieces.append(king([8,5], "black", board))
        pieces.append(queen([8,4], "black", board))
    
        for piece in pieces:
            board.placePiece(piece.getPosition(), piece)
        
        
    
        