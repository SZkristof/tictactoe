import os
import colours


def drawBoard(board):
    
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