from mainfunc import *
import random
import sys
from colours import *
from random import uniform
from design import *


def name_player1():
    global player1
    player1 = input("Player 1 enter your name (max 10 characters): ")
    try:
        if len(player1) <= 10:
            return player1
        else:
            raise ValueError
    except ValueError:
        print("Invalid name format, please try again.")
        name_player1()


def name_player2():
    global player2
    player2 = input("Player 2 enter your name (max 10 characters): ")
    try:
        if len(player2) <= 10:
            return player2
        else:
            raise ValueError
    except ValueError:
        print("Invalid name format, please try again.")
        name_player2()


def inputPlayerLetter():
    player1 = name_player1()
    name_player2()
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print(yellow + ', do you want to be X or O?')
        letter = input().upper()
    if letter == 'X':
        return [blue + 'X',  red + 'O']
    else:
        return [red + 'O',  blue + 'X']


def inputPlayer2Letter():
    if inputPlayerLetter() == "X":
        print ("You will be O")
        return ["\033[1;31mO", "X"]
    else:
        print ("You are X.")
        return ["X", "\033[1;31mO"]


def makeMove(board, letter, move):
    board[move] = letter


def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        your_move()
        move = input()
    return int(move)
