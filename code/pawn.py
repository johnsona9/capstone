from board import board

class pawn(object):
    
    rank = 0
    file = 0
    color = None
    board = None
    
    def __init__(self, position, color, board):
        self.file = position[0]
        self.rank = position[1]
        self.color = color
        self.board = board
    
    def attackedSquares(self):
        
        attacking = []
        finalAttacking = []
        attacking.append((self.file + 1, self.rank + 1))
        attacking.append((self.file - 1, self.rank + 1))
        
        for square in attacking:
            if (square[0] > 0 and square[0] < 9 and square[1] > 0 and square[1] < 9):
                finalAttacking.append(square)
        return finalAttacking