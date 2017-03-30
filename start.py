from design import *
from colours import *


def start():
    start = ("Please type START to start the game: ")
    for x in start:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.01)
    user_input = input("")
    return user_input


def start_game():
    print ('\nWelcome to...\n')
    front_line()
    if start() == "START":
        first_line = ("Loading . . . \n")
        for x in first_line:
            print(x, end='')
            sys.stdout.flush()
            time.sleep(0.1)


