<<<<<<< Local Changes
<<<<<<< Local Changes
import chess
import smbus
import time
from pystockfish import *
from multiprocessing import Process
from datetime import datetime
from subprocess import Popen, PIPE

board = chess.Board()
bus = smbus.SMBus(1)
address = 0x04
delay = 0.0005

moves = []
engine = Engine(depth=10)

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
            data = [0, 64 + pos]
        elif value == 0 and isAttacked:
        	data = [0, 192 + pos]
        elif value > 0:
        	data = [0, 128 + pos]
        else:
        	data = [0, pos]
        try:
		for i in data:
			bus.write_byte(address, i)
        except IOError:
		p1 = Popen("i2cdetect -y 1", stdout = PIPE)
		p2 = Popen("less", stdin = p1.stdout)

def main():
    lighter()
    while 1:
        runStockfish()
	    f = open('timing.csv', 'a')
        fromSquare = raw_input("Piece moving from square: ")
        toSquare = raw_input("Piece moving to square: ")
        move = chess.Move(chess.SQUARE_NAMES.index(fromSquare), chess.SQUARE_NAMES.index(toSquare))
        while move not in board.legal_moves:
            print "You made an illegal move, please try again."
            fromSquare = raw_input("Piece moving from square: ")
            toSquare = raw_input("Piece moving to square: ")
            move = chess.Move(chess.SQUARE_NAMES.index(fromSquare), chess.SQUARE_NAMES.index(toSquare))
        startTime = datetime.now()
        board.push(move)
        lighter()
        moves.append(move.uci())
        f.write(str(datetime.now() - startTime) + ", ")
        f.close
        print board
        
        
def runStockfish():
    engine.setposition(moves)
    p = Process(target=bestMove)
    p.start()
    p.join()
        
def bestMove():
    move = engine.bestmove()["move"]
    fromSquare = move[:2]
    toSquare = move[2:]
    bus.write_byte_data(address, 0, 1)
    time.sleep(delay)
    bus.write_byte_data(address, 0, chess.SQUARE_NAMES.index(fromSquare))
    time.sleep(delay)
    bus.write_byte_data(address, 0, 2)
    time.sleep(delay)
    bus.write_byte_data(address, 0, chess.SQUARE_NAMES.index(toSquare))


main()
