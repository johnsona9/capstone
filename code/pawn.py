from board import board
from piece import piece
class pawn(piece):
    
    def tag(self):
        if self.color == "white":
            return "wP"
        elif self.color == "black":
            return "bP"
    
    def attackedSquares(self):
        
        attacking = []
        finalAttacking = []
        if self.getColor() == "white":
            attacking.append((self.rank + 1, self.file + 1))
            attacking.append((self.rank + 1, self.file - 1))
        elif self.getColor() == "black":
            attacking.append((self.rank - 1, self.file + 1))
            attacking.append((self.rank - 1, self.file - 1))
        
        for square in attacking:
            if (square[0] > 0 and square[0] < 9 and square[1] > 0 and square[1] < 9):
                finalAttacking.append(square)
        return finalAttacking