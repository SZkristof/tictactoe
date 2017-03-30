from mainfunc import *
import random
import sys
from colours import *
from random import uniform
from design import *


def victory():
    print(green + str(player1) + " has won the game!" + colour_end)
    time.sleep(1.5)


def victory2():
    print (green + str(player2) + " has won the game!" + colour_end)
    time.sleep(1.5)


def your_move():
    print(colours.yellow + 'What is your next move?' + colours.colour_end)


def whoGoesFirst():
    if random.randint(0, 1) == 0:
        print (red + str(player1) + ' comes first..')
        time.sleep(2)
        return 'player1'
    else:
        print (red + str(player2) + ' comes first..')
        time.sleep(2)
        return 'player2'


def name_player1():
    global player1
    player1 = input(yellow + "Player 1 enter your name (max 10 characters): " + colour_end)
    try:
        if len(player1) <= 10:
            return player1
        else:
            raise ValueError
    except ValueError:
        print(yellow + "Invalid name format, please try again." + colour_end)
        name_player1()


def name_player2():
    global player2
    player2 = input(yellow + "Player 2 enter your name (max 10 characters): " + colour_end)
    try:
        if len(player2) <= 10:
            return player2
        else:
            raise ValueError
    except ValueError:
        print(yellow + "Invalid name format, please try again." + colour_end)
        name_player2()


def inputPlayerLetter():
    player1 = name_player1()
    player2 = name_player2()
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print(blue + str(player1) + ', do you want to be X or O?')
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
