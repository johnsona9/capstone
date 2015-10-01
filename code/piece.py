class piece(object):
    
    rank = 0
    file = 0
    color = None
    board = None
    
    def __init__(self, position, color, board):
        self.rank = position[0]
        self.file = position[1]
        self.color = color
        self.board = board
        
    def getColor(self):
        return self.color
        
    def getPosition(self):
        return (self.rank, self.file)
        
    def attackedSquares(self):
        return 0
        
    def movePiece(self, newPosition):
        self.board.movePiece(self, newPosition)
        self.rank = newPosition[0]
        self.file = newPosition[1]