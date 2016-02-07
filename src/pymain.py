import chess
import smbus
import time
from pystockfish import *
from multiprocessing import Process
from datetime import datetime

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
       		time.sleep(delay)
		bus.write_block_data(address, 0, [0, 64 + pos])
        elif value == 0 and isAttacked:
        	time.sleep(delay)
		bus.write_block_data(address, 0, [0, 192 + pos])
        elif value > 0:
		time.sleep(delay)        	
		bus.write_block_data(address, 0, [0, 128 + pos])
        else:
        	time.sleep(delay)
		bus.write_block_data(address, 0, [0, pos])

def main():
    while 1:
        lighter()
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
        
main()
