from board import board
from piece import piece
class rook(piece):
    
    def tag(self):
        if self.color == "white":
            return "wR"
        elif self.color == "black":
            return "bR"
    
    def attackedSquares(self):
        attacking = []
        finalAttacking = []
        
        #right side
        x = 1
        position = (self.rank, self.file + x)
        while position[0] > 0 and position[0] < 9 and position[1] > 0 and position[1] < 9:
            if self.board.isFull(position):
                attacking.append(position)
                break #from while
            else:
                attacking.append(position)
            x += 1
            position = (self.file + x, self.rank)
            
        #left side
        x = 1
        position = (self.rank, self.file - x)
        while position[0] > 0 and position[0] < 9 and position[1] > 0 and position[1] < 9:
            if self.board.isFull(position):
                attacking.append(position)
                break #from while
            else:
                attacking.append(position)
            x += 1
            position = (self.file - x, self.rank)
            
        #up 
        x = 1
        position = (self.rank + x, self.file)
        while position[0] > 0 and position[0] < 9 and position[1] > 0 and position[1] < 9:
            if self.board.isFull(position):
                attacking.append(position)
                break #from while
            else:
                attacking.append(position)
            x += 1
            position = (self.file, self.rank + x)
            
        #down 
        x = 1
        position = (self.rank - x, self.file)
        while position[0] > 0 and position[0] < 9 and position[1] > 0 and position[1] < 9:
            if self.board.isFull(position):
                attacking.append(position)
                break #from while
            else:
                attacking.append(position)
            x += 1
            position = (self.file, self.rank - x)
            
        for square in attacking:
            if (square[0] > 0 and square[0] < 9 and square[1] > 0 and square[1] < 9):
                finalAttacking.append(square)

        return finalAttacking