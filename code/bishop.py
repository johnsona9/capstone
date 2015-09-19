from board import board

class bishop(object):
    
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
        
        #right up diagonal
        x = 1
        position = (self.file + x, self.rank + x)
        while position[0] > 0 and position[0] < 9 and position[1] > 0 and position[1] < 9:
            if self.board.isFull(position):
                attacking.append(position)
                break #from while
            else:
                attacking.append(position)
            x += 1
            position = (self.file + x, self.rank + x)
        
        #right down diagonal
        x = 1
        position = (self.file + x, self.rank - x)
        while position[0] > 0 and position[0] < 9 and position[1] > 0 and position[1] < 9:
            if self.board.isFull(position):
                attacking.append(position)
                break #from while
            else:
                attacking.append(position)
            x += 1
            position = (self.file + x, self.rank - x)
        
        #left up diagonal
        x = 1
        position = (self.file - x, self.rank + x)
        while position[0] > 0 and position[0] < 9 and position[1] > 0 and position[1] < 9:
            if self.board.isFull(position):
                attacking.append(position)
                break #from while
            else:
                attacking.append(position)
            x += 1
            position = (self.file - x, self.rank + x)
            
        #left down diagonal
        x = 1
        position = (self.file - x, self.rank - x)
        while position[0] > 0 and position[0] < 9 and position[1] > 0 and position[1] < 9:
            print self.board.isFull(position)
            if self.board.isFull(position):
                attacking.append(position)
                break #from while
            else:
                attacking.append(position)
            x += 1
            position = (self.file - x, self.rank - x)

        for square in attacking:
            if (square[0] > 0 and square[0] < 9 and square[1] > 0 and square[1] < 9):
                finalAttacking.append(square)

        return finalAttacking
        