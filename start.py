from design import *
from colours import *
from main import *
from sys import *


def start():
    start = ("Please type START to start the game: ")
    for x in start:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.01)
    user_input = input("").capitalize
    return user_input


def start_game():
    print ('\nWelcome to...\n')
    # front_line()
    start_game2()


def start_game2():

    try:
        if start() == "START":
            first_line = ("Loading . . . \n")
            for x in first_line:
                print(x, end='')
                sys.stdout.flush()
                time.sleep(0.1)
            user_input = input("").capitalize
            return user_input
        else:
            raise ValueError

    except ValueError:
        print("Please type 'START' to start the game")
        start_game2()


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
