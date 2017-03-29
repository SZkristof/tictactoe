import random
import time
import sys
from random import uniform
from design import *
from inputs import *


def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'player1'
    else:
        return 'player2'


def isWinner(bo, le):
    return (
        (bo[7] == le and bo[8] == le and bo[9] == le) or
        (bo[4] == le and bo[5] == le and bo[6] == le) or
        (bo[1] == le and bo[2] == le and bo[3] == le) or
        (bo[7] == le and bo[4] == le and bo[1] == le) or
        (bo[8] == le and bo[5] == le and bo[2] == le) or
        (bo[9] == le and bo[6] == le and bo[3] == le) or
        (bo[7] == le and bo[5] == le and bo[3] == le) or
        (bo[9] == le and bo[5] == le and bo[1] == le)
        )


def isSpaceFree(board, move):
    return board[move] == ' '


def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True
