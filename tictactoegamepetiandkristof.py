import random
import time
import sys
from random import uniform
import colours


def drawBoard(board):

    import os
    os.system('clear')

    print(colours.yellow + '│¯¯¯¯¯││¯¯¯¯¯││¯¯¯¯¯│')
    print(colours.yellow + '│  ' + board[7] + colours.yellow + '  ││  '  + board[8] + colours.yellow + '  ││  ' + board[9] + colours.yellow + '  │')
    print(colours.yellow + '│_____││_____││_____│')

    print(colours.yellow + '│¯¯¯¯¯││¯¯¯¯¯││¯¯¯¯¯│')
    print(colours.yellow + '│  ' + board[4] + colours.yellow + '  ││  '  + board[5] + colours.yellow + '  ││  ' + board[6]+ colours.yellow + '  │')
    print(colours.yellow + '│_____││_____││_____│')

    print(colours.yellow + '│¯¯¯¯¯││¯¯¯¯¯││¯¯¯¯¯│')
    print(colours.yellow + '│  ' + board[1] + colours.yellow + '  ││  '  + board[2] + colours.yellow + '  ││  ' + board[3]+ colours.yellow + '  │')
    print(colours.yellow + '│     ││     ││     │')
    print(colours.yellow + ' ¯¯¯¯¯  ¯¯¯¯¯  ¯¯¯¯¯ ')


def inputPlayerLetter():

    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('colours.yellow + ⓨⓞⓤ ⓦⓘⓛⓛ ⓑⓔ ⓟⓛⓐⓨⓔⓡ ⓞⓝⓔ. ⓓⓞ ⓨⓞⓤ ⓦⓐⓝⓣ ⓣⓞ ⓑⓔ │ⓧ│ ⓞⓡ │ⓩ│?')
        letter = input().upper()
    if letter == 'X':
        return ['\033[1;34mX', '\033[1;31mO']
    else:
        return ['\033[1;31mO', '\033[1;34mX']


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
        print('colours.yellow +                ___       __          __        __           ___     ___           __        ___ __ ')
        print('colours.yellow + |  | |__|  /\   |     | /__`    \ / /  \ |  | |__)    |\ | |__  \_/  |      |\/| /  \ \  / |__   _|')
        print('colours.yellow + |/\| |  | /~~\  |     | .__/     |  \__/ \__/ |  \    | \| |___ / \  |      |  | \__/  \/  |___  . ')
        move = input()
    return int(move)


def getPlayer2Move(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('colours.yellow +                ___       __          __        __           ___     ___           __        ___ __ ')
        print('colours.yellow + |  | |__|  /\   |     | /__`    \ / /  \ |  | |__)    |\ | |__  \_/  |      |\/| /  \ \  / |__   _|')
        print('colours.yellow + |/\| |  | /~~\  |     | .__/     |  \__/ \__/ |  \    | \| |___ / \  |      |  | \__/  \/  |___  . ')
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
    line_1 = (colours.red + "████████╗██╗ ██████╗    ████████╗ █████╗  ██████╗    \033[1;32m████████╗ ██████╗ ███████╗")
    for x in line_1:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.005)
    time.sleep(0.1)
    print("")
    line_2 = (colours.red + "╚══██╔══╝██║██╔════╝    ╚══██╔══╝██╔══██╗██╔════╝    \033[1;32m╚══██╔══╝██╔═══██╗██╔════╝")
    for x in line_2:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.005)
    time.sleep(0.1)
    print("")
    line_3 = (colours.red + "   ██║   ██║██║            ██║   ███████║██║          \033[1;32m  ██║   ██║   ██║█████╗  ")
    for x in line_3:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.005)    
    time.sleep(0.1)
    print("")
    line_4 = (colours.red + "   ██║   ██║██║            ██║   ██╔══██║██║          \033[1;32m  ██║   ██║   ██║██╔══╝  ")
    for x in line_4:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.005)
    time.sleep(0.1)
    print("")
    line_5 = (colours.red + "   ██║   ██║╚██████╗       ██║   ██║  ██║╚██████╗     \033[1;32m  ██║   ╚██████╔╝███████╗")
    for x in line_5:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.005)
    time.sleep(0.1)
    print("")
    line_6 = (colours.red + "   ╚═╝   ╚═╝ ╚═════╝       ╚═╝   ╚═╝  ╚═╝ ╚═════╝     \033[1;32m  ╚═╝    ╚═════╝ ╚══════╝")
    for x in line_6:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.005)
    time.sleep(2)
    print("\n" *5)

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

                print('colours.yellow + ██╗   ██╗██╗ ██████╗████████╗ ██████╗ ██████╗ ██╗   ██╗')
                print('colours.yellow + ██║   ██║██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝')
                print('colours.yellow + ██║   ██║██║██║        ██║   ██║   ██║██████╔╝ ╚████╔╝')
                print('colours.yellow + ╚██╗ ██╔╝██║██║        ██║   ██║   ██║██╔══██╗  ╚██╔╝ ')
                print('colours.yellow +  ╚████╔╝ ██║╚██████╗   ██║   ╚██████╔╝██║  ██║   ██║  ')
                print('colours.yellow +   ╚═══╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝ ')
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

                print('colours.yellow + ██╗   ██╗██╗ ██████╗████████╗ ██████╗ ██████╗ ██╗   ██╗')
                print('colours.yellow + ██║   ██║██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝')
                print('colours.yellow + ██║   ██║██║██║        ██║   ██║   ██║██████╔╝ ╚████╔╝')
                print('colours.yellow + ╚██╗ ██╔╝██║██║        ██║   ██║   ██║██╔══██╗  ╚██╔╝ ')
                print('colours.yellow +  ╚████╔╝ ██║╚██████╗   ██║   ╚██████╔╝██║  ██║   ██║  ')
                print('colours.yellow +   ╚═══╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝ ')
                print("\n"*3)
                time.sleep(1.5)
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player1'
