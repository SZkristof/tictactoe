import time
import sys
import colours
import os


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


def front_line():
    line_1 = (colours.red + "████████╗██╗ ██████╗ " + colours.colour_end + "   ████████╗ █████╗  ██████╗    " + colours.green + "████████╗ ██████╗ ███████╗")
    for x in line_1:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.005)
    time.sleep(0.1)
    print("")
    line_2 = (colours.red + "╚══██╔══╝██║██╔════╝  " + colours.colour_end + "  ╚══██╔══╝██╔══██╗██╔════╝    " + colours.green + "╚══██╔══╝██╔═══██╗██╔════╝")
    for x in line_2:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.005)
    time.sleep(0.1)
    print("")
    line_3 = (colours.red + "   ██║   ██║██║     " + colours.colour_end + "       ██║   ███████║██║          " + colours.green + "  ██║   ██║   ██║█████╗  ")
    for x in line_3:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.005)
    time.sleep(0.1)
    print("")
    line_4 = (colours.red + "   ██║   ██║██║      " + colours.colour_end + "      ██║   ██╔══██║██║          " + colours.green + "  ██║   ██║   ██║██╔══╝  ")
    for x in line_4:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.005)
    time.sleep(0.1)
    print("")
    line_5 = (colours.red + "   ██║   ██║╚██████╗   " + colours.colour_end + "    ██║   ██║  ██║╚██████╗     " + colours.green + "  ██║   ╚██████╔╝███████╗")
    for x in line_5:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.005)
    time.sleep(0.1)
    print("")
    line_6 = (colours.red + "   ╚═╝   ╚═╝ ╚═════╝    " + colours.colour_end + "   ╚═╝   ╚═╝  ╚═╝ ╚═════╝     " + colours.green + "  ╚═╝    ╚═════╝ ╚══════╝" + colours.colour_end)
    for x in line_6:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.005)
    time.sleep(0.2)
    print("\n" *5)





