class piece(object):
    
    rank = 0
    file = 0
    color = None
    board = None
    
    def __init__(self, position, color, board):
        self.file = position[0]
        self.rank = position[1]
        self.color = color
        
    def getColor(self):
        return self.color
        
    def getPosition(self):
        return (self.file, self.rank)