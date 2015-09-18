class board(object):
    
    
    
    def __init__(self):
        self.squares = [[], [], [], [], [], [], [], []]
        for rank in self.squares:
            for x in range(0,8):
                rank.append(None)
                
    def placePiece(self, position, piece):
        self.squares[position[0]][position[1]] = piece
        print self.squares
    # def getAttacked(self):
#
#     def setupGame(self):
        
    def isFull(self, position):
        return not self.squares[position[0]][position[1]]
        #if the given position has a piece return true