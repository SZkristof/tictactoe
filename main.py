from design import *
from inputs import *
from mainfunc import *
from colours import *


def main():

    while True:

        front_line()
        theBoard = [' '] * 10
        turn = whoGoesFirst()
        playerLetter, player2Letter = inputPlayerLetter()
        gameIsPlaying = True

        while gameIsPlaying:

            if turn == "player1":
                drawBoard(theBoard)
                move = getPlayerMove(theBoard)
                makeMove(theBoard, playerLetter, move)

                if isWinner(theBoard, playerLetter):
                    drawBoard(theBoard)
                    victory()
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
                    victory()
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'player1'

if __name__ == "__main__":
    main()
