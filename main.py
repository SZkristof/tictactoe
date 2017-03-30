from design import *
from inputs import *
from mainfunc import *
from colours import *
from start import *


def main():
    lol()


def lol():

    while True:

        start_game()
        theBoard = [' '] * 10
        playerLetter, player2Letter = inputPlayerLetter()
        turn = whoGoesFirst()
        gameIsPlaying = True
        
        while True:

            while gameIsPlaying:

                if turn == "player1":
                    drawBoard(theBoard)
                    move = getPlayerMove(theBoard)
                    makeMove(theBoard, playerLetter, move)

                    if isWinner(theBoard, playerLetter):
                        drawBoard(theBoard)
                        victory()
                        gameIsPlaying = False
                        game_finish()
                        main()
                    else:
                        if isBoardFull(theBoard):
                            drawBoard(theBoard)
                            print('The game is a tie!')
                            game_finish()
                        else:
                            turn = 'player2'
                else:
                    drawBoard(theBoard)
                    move = getPlayerMove(theBoard)
                    makeMove(theBoard, player2Letter, move)

                    if isWinner(theBoard, player2Letter):
                        drawBoard(theBoard)
                        victory2()
                        gameIsPlaying = False
                        game_finish()
                        main()
                    else:
                        if isBoardFull(theBoard):
                            drawBoard(theBoard)
                            print('The game is a tie!')
                            game_finish()
                        else:
                            turn = 'player1'

if __name__ == "__main__":
    main()