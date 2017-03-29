import random
import time
import sys
from random import uniform
import colours
from printboard import drawBoard
import smalls


def inputPlayerLetter():

    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print(colours.yellow + 'Do you want to be X or O?')
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
        smalls.your_move()
        move = input()
    return int(move)


def isSpaceFree(board, move):
    return board[move] == ' '


def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True