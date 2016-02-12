import chess
import smbus
import time
from pystockfish import *
from multiprocessing import Process
from datetime import datetime
from subprocess import Popen, PIPE
import sys

board = chess.Board()
bus = smbus.SMBus(1)
address = 0x04
delay = 0.0005

moves = []
engine = Engine(depth=10)
stockfish = False
if (len(sys.argv) > 1 and int(sys.argv[1]) == 1):
    stockfish = True


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
        if (stockfish):
            bus.write_byte(address, 3)
            time.sleep(delay)
            bus.write_byte(address, 0)
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
                time.sleep(delay)
                bus.write_byte(address, i)
        except IOError:
		    Popen("i2cdetect -y 1>/dev/null", shell=True)


def main():
    lighter()
    while 1:
        if (stockfish):
            runStockfish()
        f = open('timing.csv', 'a')
        move = requestMove()
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


def checkPromotions(fromSquare, toSquare):
    if (board.piece_at(chess.SQUARE_NAMES.index(fromSquare)) == chess.Piece(chess.PAWN, chess.WHITE) and toSquare[1] == '8') or (board.piece_at(chess.SQUARE_NAMES.index(fromSquare)) == chess.Piece(chess.PAWN, chess.BLACK) and toSquare[1] == '1'):
        return promotionQuery()
    else:
        return 0

def requestMove():
    fromSquare = raw_input("Piece moving from square: ")
    while fromSquare not in chess.SQUARE_NAMES:
        print "You entered a value that is not a square, please enter another square."
        fromSquare = raw_input("Piece moving from square: ")
    toSquare = raw_input("Piece moving to square: ")
    while toSquare not in chess.SQUARE_NAMES:
        print "You entered a value that is not a square, please enter another square."
        toSquare = raw_input("Piece moving to square: ")
    promotion = checkPromotions(fromSquare, toSquare)
    if promotion == 0:
        move = chess.Move(chess.SQUARE_NAMES.index(fromSquare), chess.SQUARE_NAMES.index(toSquare))
    else:
        move = chess.Move(chess.SQUARE_NAMES.index(fromSquare), chess.SQUARE_NAMES.index(toSquare), promotion)
    while move not in board.legal_moves:
        print "You made an illegal move, please try again."
        fromSquare = raw_input("Piece moving from square: ")
        while fromSquare not in chess.SQUARE_NAMES:
            print "You entered a value that is not a square, please enter another square."
            fromSquare = raw_input("Piece moving from square: ")
        toSquare = raw_input("Piece moving to square: ")
        while toSquare not in chess.SQUARE_NAMES:
            print "You entered a value that is not a square, please enter another square."
            toSquare = raw_input("Piece moving to square: ")
        promotion = checkPromotions(fromSquare, toSquare)
        if promotion == 0:
            move = chess.Move(chess.SQUARE_NAMES.index(fromSquare), chess.SQUARE_NAMES.index(toSquare))
        else:
            move = chess.Move(chess.SQUARE_NAMES.index(fromSquare), chess.SQUARE_NAMES.index(toSquare), promotion)
    return move

def promotionQuery():
    options = {'q': 5, 'r': 4, 'b': 3, 'n': 2}
    print "Promotion options are:"
    print "q : queen"
    print "r : rook"
    print "b : bishop"
    print "n : knight"
    promotion = raw_input("What piece would you like to promote to?")
    while promotion not in options:
        print "You did not enter a legal promotion, please trt again."
        print "Promotion options are:"
        print "q : queen"
        print "r : rook"
        print "b : bishop"
        print "n : knight"
        promotion = raw_input("What piece would you like to promote to?")
    return options[promotion]

main()
