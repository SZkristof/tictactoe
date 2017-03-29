import mainfunc
import smalls
from printboard import drawBoard

while True:

    smalls.front_line()
    theBoard = [' '] * 10
    playerLetter, player2Letter = mainfunc.inputPlayerLetter()
    turn = mainfunc.whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:

        if turn == "player1":
            drawBoard(theBoard)
            move = mainfunc.getPlayerMove(theBoard)
            mainfunc.makeMove(theBoard, playerLetter, move)

            if mainfunc.isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                smalls.victory()
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
                smalls.victory()
                gameIsPlaying = False
            else:
                if mainfunc.isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player1'
