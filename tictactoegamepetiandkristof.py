import random
import time
import sys
from random import uniform


def drawBoard(board):

    import os
    os.system('clear')

    print('\033[1;33m│¯¯¯¯¯││¯¯¯¯¯││¯¯¯¯¯│\033[1;m')
    print('\033[1;33m│  \033[1;m' + board[7] + '\033[1;33m  ││  \033[1;m'    + board[8] +'\033[1;33m  ││  \033[1;m' + board[9] +'\033[1;33m  │\033[1;m')
    print('\033[1;33m│_____││_____││_____│\033[1;m')

    print('\033[1;33m│¯¯¯¯¯││¯¯¯¯¯││¯¯¯¯¯│')
    print('\033[1;33m│  \033[1;m' + board[4] + '\033[1;33m  ││  \033[1;m'  + board[5] +'\033[1;33m  ││  \033[1;m' + board[6]+'\033[1;33m  │\033[1;m')
    print('\033[1;33m│_____││_____││_____│\033[1;m')

    print('\033[1;33m│¯¯¯¯¯││¯¯¯¯¯││¯¯¯¯¯│\033[1;m')
    print('\033[1;33m│  \033[1;m' + board[1] + '\033[1;33m  ││  \033[1;m'  + board[2] +'\033[1;33m  ││  \033[1;m' + board[3]+'\033[1;33m  │\033[1;m')
    print('\033[1;33m│     ││     ││     │\033[1;m')
    print('\033[1;33m ¯¯¯¯¯  ¯¯¯¯¯  ¯¯¯¯¯\033[1;m')


def inputPlayerLetter():

    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('\033[1;33mⓨⓞⓤ ⓦⓘⓛⓛ ⓑⓔ ⓟⓛⓐⓨⓔⓡ ⓞⓝⓔ. ⓓⓞ ⓨⓞⓤ ⓦⓐⓝⓣ ⓣⓞ ⓑⓔ │ⓧ│ ⓞⓡ │ⓩ│?\033[1;m')
        letter = input().upper()
    if letter == 'X':
        return ['\033[1;34mX\033[1;m', '\033[1;31mO\033[1;m']
    else:
        return ['\033[1;31mO\033[1;m', '\033[1;34mX\033[1;m']


def inputPlayer2Letter():
    if inputPlayerLetter() == "X":
        print ("You will be O")
        return ["\033[1;31mO\033[1;m", "X"]
    else:
        print ("You are X.")
        return ["X", "\033[1;31mO\033[1;m"]


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
        print('\033[1;33m               ___       __          __        __           ___     ___           __        ___ __ \033[1;m')
        print('\033[1;33m|  | |__|  /\   |     | /__`    \ / /  \ |  | |__)    |\ | |__  \_/  |      |\/| /  \ \  / |__   _|\033[1;m')
        print('\033[1;33m|/\| |  | /~~\  |     | .__/     |  \__/ \__/ |  \    | \| |___ / \  |      |  | \__/  \/  |___  . \033[1;m')
        move = input()
    return int(move)


def getPlayer2Move(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('\033[1;33m               ___       __          __        __           ___     ___           __        ___ __ \033[1;m')
        print('\033[1;33m|  | |__|  /\   |     | /__`    \ / /  \ |  | |__)    |\ | |__  \_/  |      |\/| /  \ \  / |__   _|\033[1;m')
        print('\033[1;33m|/\| |  | /~~\  |     | .__/     |  \__/ \__/ |  \    | \| |___ / \  |      |  | \__/  \/  |___  . \033[1;m')
        move = input()
    return int(move)


def isSpaceFree(board, move):
    return board[move] == ' '


def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

while True:
    line_1 = ("\033[1;31m████████╗██╗ ██████╗\033[1;m    ████████╗ █████╗  ██████╗\033[1;m    \033[1;32m████████╗ ██████╗ ███████╗\033[1;m")
    for x in line_1:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.005)
    time.sleep(0.1)
    print("")
    line_2 = ("\033[1;31m╚══██╔══╝██║██╔════╝\033[1;m    ╚══██╔══╝██╔══██╗██╔════╝\033[1;m    \033[1;32m╚══██╔══╝██╔═══██╗██╔════╝\033[1;m")
    for x in line_2:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.005)
    time.sleep(0.1)
    print("")
    line_3 = ("\033[1;31m   ██║   ██║██║     \033[1;m       ██║   ███████║██║     \033[1;m     \033[1;32m  ██║   ██║   ██║█████╗  \033[1;m")
    for x in line_3:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.005)    
    time.sleep(0.1)
    print("")
    line_4 = ("\033[1;31m   ██║   ██║██║     \033[1;m       ██║   ██╔══██║██║     \033[1;m     \033[1;32m  ██║   ██║   ██║██╔══╝  \033[1;m")
    for x in line_4:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.005)
    time.sleep(0.1)
    print("")
    line_5 = ("\033[1;31m   ██║   ██║╚██████╗\033[1;m       ██║   ██║  ██║╚██████╗\033[1;m     \033[1;32m  ██║   ╚██████╔╝███████╗\033[1;m")
    for x in line_5:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.005)
    time.sleep(0.1)
    print("")
    line_6 = ("\033[1;31m   ╚═╝   ╚═╝ ╚═════╝\033[1;m       ╚═╝   ╚═╝  ╚═╝ ╚═════╝\033[1;m     \033[1;32m  ╚═╝    ╚═════╝ ╚══════╝\033[1;m")
    for x in line_6:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.005)
    time.sleep(2)
    print("")
    print("")
    print("")

    theBoard = [' '] * 10
    playerLetter, player2Letter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == "player1":
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('────────────────█████████───────────────')
                print('──────────────█████████████─────────────')
                print('───────────███████████████████──────────')
                print('────────────────────────────────────────')
                print('────────████████████████████████────────')
                print('────────████████████████████████────────')
                print('────────────────────────────────────────')
                print('█████████─████████████████████─█████████')
                print('█████████─████████████████████─█████████')
                print('███───────████████────████████───────███')
                print('███───────██████───██───██████───────███')
                print('─███──────█████──████────█████──────███─')
                print('──███─────████─────██─────████─────███──')
                print('───███────████─────██─────████────███───')
                print('────███───█████────██────█████───███────')
                print('─────███──█████────██────█████──███─────')
                print('──────███─███████──────███████─███──────')
                print('───────██─████████████████████─██───────')
                print('────────█─████████████████████─█────────')
                print('────────────────────────────────────────')
                print('──────────████████████████████──────────')
                print('───────────██████████████████───────────')
                print('─────────────██████████████─────────────')
                print('───────────────███████████──────────────')
                print('────────────────────────────────────────')
                print('────────────────█████████───────────────')
                print('──────────────█████████████─────────────')

                print('\033[1;33m██╗   ██╗██╗ ██████╗████████╗ ██████╗ ██████╗ ██╗   ██╗\033[1;m')
                print('\033[1;33m██║   ██║██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝\033[1;m')
                print('\033[1;33m██║   ██║██║██║        ██║   ██║   ██║██████╔╝ ╚████╔╝\033[1;m')
                print('\033[1;33m╚██╗ ██╔╝██║██║        ██║   ██║   ██║██╔══██╗  ╚██╔╝ \033[1;m')
                print('\033[1;33m ╚████╔╝ ██║╚██████╗   ██║   ╚██████╔╝██║  ██║   ██║  \033[1;m')
                print('\033[1;33m  ╚═══╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝ \033[1;m')
                print("")
                print("")
                print("")
                print("")
                print("")
                print("")
                time.sleep(1.5)
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player2'

        else:
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, player2Letter, move)

            if isWinner(theBoard, player2Letter):
                drawBoard(theBoard)
                print('────────────────█████████───────────────')
                print('──────────────█████████████─────────────')
                print('───────────███████████████████──────────')
                print('────────────────────────────────────────')
                print('────────████████████████████████────────')
                print('────────████████████████████████────────')
                print('────────────────────────────────────────')
                print('█████████─████████████████████─█████████')
                print('█████████─████████████████████─█████████')
                print('███───────████████────████████───────███')
                print('███───────██████───██───██████───────███')
                print('─███──────█████──████────█████──────███─')
                print('──███─────████─────██─────████─────███──')
                print('───███────████─────██─────████────███───')
                print('────███───█████────██────█████───███────')
                print('─────███──█████────██────█████──███─────')
                print('──────███─███████──────███████─███──────')
                print('───────██─████████████████████─██───────')
                print('────────█─████████████████████─█────────')
                print('────────────────────────────────────────')
                print('──────────████████████████████──────────')
                print('───────────██████████████████───────────')
                print('─────────────██████████████─────────────')
                print('───────────────███████████──────────────')
                print('────────────────────────────────────────')
                print('────────────────█████████───────────────')
                print('──────────────█████████████─────────────')

                print('\033[1;33m██╗   ██╗██╗ ██████╗████████╗ ██████╗ ██████╗ ██╗   ██╗\033[1;m')
                print('\033[1;33m██║   ██║██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝\033[1;m')
                print('\033[1;33m██║   ██║██║██║        ██║   ██║   ██║██████╔╝ ╚████╔╝\033[1;m')
                print('\033[1;33m╚██╗ ██╔╝██║██║        ██║   ██║   ██║██╔══██╗  ╚██╔╝ \033[1;m')
                print('\033[1;33m ╚████╔╝ ██║╚██████╗   ██║   ╚██████╔╝██║  ██║   ██║  \033[1;m')
                print('\033[1;33m  ╚═══╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝ \033[1;m')
                print("")
                print("")
                print("")
                print("")
                print("")
                print("")
                time.sleep(1.5)
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player1'
