from board import board
from piece import piece
class queen(piece):
    
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
            position = (self.rank, self.file + x)
            
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
            position = (self.rank, self.file - x)
            
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
            position = (self.rank + x, self.file)
            
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
            position = (self.rank - x, self.file)
            
        #right up diagonal
        x = 1
        position = (self.rank + x, self.file + x)
        while position[0] > 0 and position[0] < 9 and position[1] > 0 and position[1] < 9:
            if self.board.isFull(position):
                attacking.append(position)
                break #from while
            else:
                attacking.append(position)
            x += 1
            position = (self.rank + xself.file + x)
        
        #right down diagonal
        x = 1
        position = (self.rank - x, self.file + x)
        while position[0] > 0 and position[0] < 9 and position[1] > 0 and position[1] < 9:
            if self.board.isFull(position):
                attacking.append(position)
                break #from while
            else:
                attacking.append(position)
            x += 1
            position = (self.rank - x, self.file + x)
        
        #left up diagonal
        x = 1
        position = (self.rank + x, self.file - x)
        while position[0] > 0 and position[0] < 9 and position[1] > 0 and position[1] < 9:
            if self.board.isFull(position):
                attacking.append(position)
                break #from while
            else:
                attacking.append(position)
            x += 1
            position = (self.rank + x, self.file - x)
            
        #left down diagonal
        x = 1
        position = (self.rank - x, self.file - x)
        while position[0] > 0 and position[0] < 9 and position[1] > 0 and position[1] < 9:
            if self.board.isFull(position):
                attacking.append(position)
                break #from while
            else:
                attacking.append(position)
            x += 1
            position = (self.rank - x, self.file - x)
            
        for square in attacking:
            if (square[0] > 0 and square[0] < 9 and square[1] > 0 and square[1] < 9):
                finalAttacking.append(square)

        return finalAttacking