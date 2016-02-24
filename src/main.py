import time
from subprocess import Popen
import sys
from multiprocessing import Process


import chess
import smbus
from pystockfish import *


BOARD = chess.Board()
BUS = smbus.SMBus(1)
ADDRESS = 0x04
DELAY = 0.0005

lastMove = False
MOVES = []
ENGINE = Engine(depth=10)
STOCKFISH = False
if len(sys.argv) > 1 and int(sys.argv[1]) == 1:
    STOCKFISH = True


def lighter():
    if BOARD.is_game_over():
        if BOARD.is_checkmate():
            if lastMove:
                single_color("green")
            else:
                single_color("red")
        elif BOARD.is_stalemate():
            single_color("blue")

    else:
        for x in chess.SQUARES:
            isAttacked = False
            whiteAttacks = len(BOARD.attackers(chess.WHITE, chess.SQUARES[x]))
            if whiteAttacks > 0:
                isAttacked = True
            blackAttacks = len(BOARD.attackers(chess.BLACK, chess.SQUARES[x]))
            value = whiteAttacks - blackAttacks
            rank = x / 8
            column = x % 8
            pos = rank * 8 + column
            if STOCKFISH:
                time.sleep(DELAY)
                BUS.write_byte(ADDRESS, 3)
                time.sleep(DELAY)
                BUS.write_byte(ADDRESS, 0)
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
                    time.sleep(DELAY)
                    BUS.write_byte(ADDRESS, i)
            except IOError:
                Popen("i2cdetect -y 1 >/dev/null", shell=True)
                lighter()


def main():
    lighter()
    while not BOARD.is_game_over():
        if STOCKFISH:
            run_stockfish()
        move = request_move()
        BOARD.push(move)
        global lastMove
        lastMove = not lastMove
        lighter()
        MOVES.append(move.uci())
        print BOARD
    lighter()


def run_stockfish():
    ENGINE.setposition(MOVES)
    p = Process(target=best_move)
    p.start()
    p.join()


def best_move():
    move = ENGINE.bestmove()["move"]
    fromSquare = move[:2]
    toSquare = move[2:]
    time.sleep(DELAY)
    BUS.write_byte_data(ADDRESS, 0, 1)
    time.sleep(DELAY)
    BUS.write_byte_data(ADDRESS, 0, chess.SQUARE_NAMES.index(fromSquare))
    time.sleep(DELAY)
    BUS.write_byte_data(ADDRESS, 0, 2)
    time.sleep(DELAY)
    BUS.write_byte_data(ADDRESS, 0, chess.SQUARE_NAMES.index(toSquare))


def check_promotions(fromSquare, toSquare):
    if (BOARD.piece_at(chess.SQUARE_NAMES.index(fromSquare)) == chess.Piece(chess.PAWN, chess.WHITE) and toSquare[1] == '8') or (BOARD.piece_at(chess.SQUARE_NAMES.index(fromSquare)) == chess.Piece(chess.PAWN, chess.BLACK) and toSquare[1] == '1'):
        return promotion_query()
    else:
        return 0

def request_move():
    fromSquare = raw_input("Piece moving from square: ")
    while fromSquare not in chess.SQUARE_NAMES:
        print "You entered a value that is not a square, please enter another square."
        fromSquare = raw_input("Piece moving from square: ")
    toSquare = raw_input("Piece moving to square: ")
    while toSquare not in chess.SQUARE_NAMES:
        print "You entered a value that is not a square, please enter another square."
        toSquare = raw_input("Piece moving to square: ")
    promotion = check_promotions(fromSquare, toSquare)
    if promotion == 0:
        move = chess.Move(chess.SQUARE_NAMES.index(fromSquare), chess.SQUARE_NAMES.index(toSquare))
    else:
        move = chess.Move(chess.SQUARE_NAMES.index(fromSquare), chess.SQUARE_NAMES.index(toSquare), promotion)
    while move not in BOARD.legal_moves:
        print "You made an illegal move, please try again."
        fromSquare = raw_input("Piece moving from square: ")
        while fromSquare not in chess.SQUARE_NAMES:
            print "You entered a value that is not a square, please enter another square."
            fromSquare = raw_input("Piece moving from square: ")
        toSquare = raw_input("Piece moving to square: ")
        while toSquare not in chess.SQUARE_NAMES:
            print "You entered a value that is not a square, please enter another square."
            toSquare = raw_input("Piece moving to square: ")
        promotion = check_promotions(fromSquare, toSquare)
        if promotion == 0:
            move = chess.Move(chess.SQUARE_NAMES.index(fromSquare), chess.SQUARE_NAMES.index(toSquare))
        else:
            move = chess.Move(chess.SQUARE_NAMES.index(fromSquare), chess.SQUARE_NAMES.index(toSquare), promotion)
    return move


def single_color(color):
    colors = {"red" : 64, "green": 128, "blue": 192}
    for x in chess.SQUARES:
        data = [0, x + colors[color]]
        try:
            for i in data:
                time.sleep(DELAY)
                BUS.write_byte(ADDRESS, i)
        except IOError:
            Popen("i2cdetect -y 1 >/dev/null", shell=True)


def promotion_query():
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
