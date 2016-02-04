import chess
import smbus

board = chess.Board()
bus = smbus.SMBus(1)
address = 0x04

def lighter():
    for x in chess.SQUARES:
        isAttacked = False
        whiteAttacks = len(board.attackers(chess.WHITE, chess.SQUARES[x]))
        if whiteAttacks > 0:
            isAttacked = True
        blackAttacks = len(board.attackers(chess.BLACK, chess.SQUARES[x]))
        value = whiteAttacks - blackAttacks
        
        rank = x / 8
        file = x % 8
        pos = rank * 8 + file
        if value < 0:
       		bus.write_byte_data(address, 0, 64 + pos)
        elif value == 0 and isAttacked:
        	bus.write_byte_data(address, 0, 192 + pos)
        elif value > 0:
        	bus.write_byte_data(address, 0, 128 + pos)
        else:
        	bus.write_byte_data(address, 0, pos)

def main():
    while 1:
        lighter()
        fromSquare = raw_input("Piece moving from square: ")
        toSquare = raw_input("Piece moving to square: ")
        move = chess.Move(chess.SQUARE_NAMES.index(fromSquare), chess.SQUARE_NAMES.index(toSquare))
        while move not in board.legal_moves:
            print "You made an illegal move, please try again."
            fromSquare = raw_input("Piece moving from square: ")
            toSquare = raw_input("Piece moving to square: ")
            move = chess.Move(chess.SQUARE_NAMES.index(fromSquare), chess.SQUARE_NAMES.index(toSquare))
        board.push(move)
        print board
        
        
main()