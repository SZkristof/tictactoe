import mainfunc
from design import *


def main():

    while True:

        front_line()
        theBoard = [' '] * 10
        turn = mainfunc.whoGoesFirst()
        playerLetter, player2Letter = mainfunc.inputPlayerLetter()
        print('The ' + turn + ' will go first.')
        gameIsPlaying = True

        while gameIsPlaying:

            if turn == "player1":
                drawBoard(theBoard)
                move = mainfunc.getPlayerMove(theBoard)
                mainfunc.makeMove(theBoard, playerLetter, move)

                if mainfunc.isWinner(theBoard, playerLetter):
                    drawBoard(theBoard)
                    victory()
                    gameIsPlaying = False
                else:
                    if mainfunc.isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'player2'
            else:
                drawBoard(theBoard)
                move = mainfunc.getPlayerMove(theBoard)
                mainfunc.makeMove(theBoard, player2Letter, move)

                if mainfunc.isWinner(theBoard, player2Letter):
                    drawBoard(theBoard)
                    victory()
                    gameIsPlaying = False
                else:
                    if mainfunc.isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'player1'

if __name__ == "__main__":
    main()