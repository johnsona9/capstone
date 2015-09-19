from piece import piece
class knight(piece):
    
    def attackedSquares(self):
        attacking = []
        finalAttacking = []
        attacking.append((self.file - 2, self.rank + 1))
        attacking.append((self.file - 2, self.rank - 1))
        attacking.append((self.file + 2, self.rank + 1))
        attacking.append((self.file + 2, self.rank - 1))
        attacking.append((self.file - 1, self.rank + 2))
        attacking.append((self.file - 1, self.rank - 2))
        attacking.append((self.file + 1, self.rank + 2))
        attacking.append((self.file + 1, self.rank - 2))
        
        for square in attacking:
            if (square[0] > 0 and square[0] < 9 and square[1] > 0 and square[1] < 9):
                finalAttacking.append(square)
                
        return finalAttacking
        