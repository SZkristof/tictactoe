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
    print (green + '\nWelcome to...\n' + colour_end)
    front_line()

    if start() == "START":
        first_line = ("Loading . . . \n")
        for x in first_line:
            print(x, end='')
            sys.stdout.flush()
            time.sleep(0.1)

    while start() != "START":
        try:
            raise ValueError

        except ValueError:
            if start() == "START":
                pass
            else:
                start()


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
        print("You selected: " + userInput + "Please Choose 'R' to restart or 'X' to exit!: ")
        game_finish()
