import random
import time
import sys
import colours
from random import uniform
from design import *


def name_player1():
    player1 = input("Player 1 enter your name (max 10 characters): ")
    if len(player1) <= 10:
        return player1


def name_player2():
    player2 = input("Player 2 enter your name (max 10 characters): ")
    if len(player2) <= 10:
        return player2


def inputPlayerLetter():
    player1 = name_player1()
    name_player2()
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print(colours.yellow + player1 + ' ,do you want to be X or O?')
        letter = input().upper()
    if letter == 'X':
        return [colours.blue + 'X', colours.red + 'O']
    else:
        return [colours.red + 'O', colours.blue + 'X']


def inputPlayer2Letter():
    if inputPlayerLetter() == "X":
        print ("You will be O")
        return ["\033[1;31mO", "X"]
    else:
        print ("You are X.")
        return ["X", "\033[1;31mO"]


def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'player1'
    else:
        return 'player2'


def makeMove(board, letter, move):
    board[move] = letter


def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
    (bo[4] == le and bo[5] == le and bo[6] == le) or 
    (bo[1] == le and bo[2] == le and bo[3] == le) or 
    (bo[7] == le and bo[4] == le and bo[1] == le) or 
    (bo[8] == le and bo[5] == le and bo[2] == le) or 
    (bo[9] == le and bo[6] == le and bo[3] == le) or 
    (bo[7] == le and bo[5] == le and bo[3] == le) or 
    (bo[9] == le and bo[5] == le and bo[1] == le)) 


def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        your_move()
        move = input()
    return int(move)


def isSpaceFree(board, move):
    return board[move] == ' '


def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True
