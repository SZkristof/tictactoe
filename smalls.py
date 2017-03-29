import time
import sys
import colours

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
    line_6 = (colours.red + "   ╚═╝   ╚═╝ ╚═════╝    " + colours.colour_end + "   ╚═╝   ╚═╝  ╚═╝ ╚═════╝     " + colours.green + "  ╚═╝    ╚═════╝ ╚══════╝")
    for x in line_6:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.005)
    time.sleep(0.2)
    print("\n" *5)


def victory():
    print(colours.yellow +' ██╗   ██╗██╗ ██████╗████████╗ ██████╗ ██████╗ ██╗   ██╗')
    print(' ██║   ██║██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝')
    print(' ██║   ██║██║██║        ██║   ██║   ██║██████╔╝ ╚████╔╝')
    print(' ╚██╗ ██╔╝██║██║        ██║   ██║   ██║██╔══██╗  ╚██╔╝ ')
    print('  ╚████╔╝ ██║╚██████╗   ██║   ╚██████╔╝██║  ██║   ██║  ')
    print('   ╚═══╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝ ' + colours.colour_end)
    print("\n"*3)
    time.sleep(1.5)


def your_move():
    print(colours.yellow + '                ___       __          __        __           ___     ___           __        ___ __ ')
    print(' |  | |__|  /\   |     | /__`    \ / /  \ |  | |__)    |\ | |__  \_/  |      |\/| /  \ \  / |__   _|')
    print(' |/\| |  | /~~\  |     | .__/     |  \__/ \__/ |  \    | \| |___ / \  |      |  | \__/  \/  |___  . ' + colours.colour_end)
