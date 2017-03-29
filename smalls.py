import time
import sys
import colours

def front_line():
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
    time.sleep(0.2)
    print("\n" *5)