from design import *
from colours import *
from main import *
from sys import *


def start():
    start = (green + "Please type START to start the game: " + colour_end)
    for x in start:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.01)
    user_input = input("")
    return user_input


def start_game():

    print ('\nWelcome to...\n')
    front_line()
    start()
    try:

        if start() == "START":
            None
        elif start() == "start":
            None
        else:
            raise ValueError

    except ValueError:
        start()

    first_line = ("Loading . . . \n")
    for x in first_line:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.1)


def game_finish():
    userInput = input("Enter 'R' to restart or 'X' to exit.").capitalize()
    try:
        if userInput == "X":
            print('Goodbye.')
            time.sleep(1.0)
            sys.exit()
        elif userInput == "R":
            None
        else:
            raise ValueError
    except ValueError:
        print("You selected: " + userInput + "Please Choose 'R' to restart or 'X' to exit!")
        game_finish()
