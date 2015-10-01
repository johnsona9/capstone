from board import board
from piece import piece
class king(piece):
        
    def tag(self):
        if self.color == "white":
            return "wK"
        elif self.color == "black":
            return "bK"
        
    def attackedSquares(self):
        
        attacking = []
        finalAttacking = []
        attacking.append((self.rank, self.file - 1))
        attacking.append((self.rank, self.file + 1))
        attacking.append((self.rank - 1, self.file))
        attacking.append((self.rank + 1, self.file))
        attacking.append((self.rank - 1, self.file - 1))
        attacking.append((self.rank + 1, self.file + 1))
        attacking.append((self.rank + 1, self.file - 1))
        attacking.append((self.rank - 1, self.file + 1))
        for square in attacking:
            
            if (square[0] > 0 and square[0] < 9 and square[1] > 0 and square[1] < 9):
                finalAttacking.append(square)
            
            #elif self.squareFull(square, self.board):
             #   attacking.remove(square)
        return finalAttacking
        #find all squares the piece is attacking reguardless of whether or not they are valid, then check to see if they are valid
        
    def squareFull(self, position, board):
        return board.isFull(position)
            