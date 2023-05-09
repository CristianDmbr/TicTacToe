# A two player game where one player represents X and the second one O.
# The game takes place on a board made up of 9 squares, each player takes a turn
# to place their X or O and the first player to make a three square line
# ( wether in a row , diagnol or column ) wins the game. However if the board is full
# and no three squared lines are made then its a draw.

# This will also be my first experince with creating an AI to play with.

import random


# This function draws the board using ASCII.
# Each parameter representing the square on the board.
def drawBoard(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])


# This functin allows the user to decide between being X or O.
def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print("Would you like to be X or O?")
        letter = input().upper()
    # If this condition is met , the player will play using X.
    if letter == 'X':
        return ['X', 'O']
    # Otherwise O
    else:
        return ['O', 'X']


# Chooses between who goes first (Computer or Player).
# The probabilities are set to 50/50.
# The random function will also state who goes first based on therandom outcome.
def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


# Board is the parameter representing the 10 strings that represent the state of the board.
# Letter is either X or O depending on what the player has decided at the beginning of the game.
# And place is the parameter responsible for positioning where the player wants to place its sign.
# When a list value is passed for the board parameter, the function's local variable is really a copy of the reference to the
# and not a copy to the list itself. So any changes to the board in the function will also be made to the original list.
# Since the parameters of letter and move are copies of the string and integer values if you moify them in this function the
# original values you used arent modified but only create local results.
def makeMove(board, letter, move):
    board[move] = letter


# bo = board
# le = letter
# This function is responsible for knowing if the player has won or not.
def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[7] == le and bo[4] == le and bo[1] == le) or
            (bo[8] == le and bo[5] == le and bo[2] == le) or
            (bo[9] == le and bo[6] == le and bo[3] == le) or
            (bo[7] == le and bo[5] == le and bo[3] == le) or
            (bo[9] == le and bo[5] == le and bo[1] == le))


# Makes of the 10 string list representing the board game.
def getBoardCopy(board):
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy


# This makes sure that the move you want to make is possible.
def isSpaceFree(board, move):
    return board[move] == ' '


# This function allows the player to interact with the game by inserting the place
# where he wants to make the next move.
# This also allows only numbers from 1 - 9 to be entered by the user.
def getPlayerMove(board):
    move = ' '
    # Split() allows to make every number from that string into a separate element.
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print("What is your next move? (1-9)")
        move = input()
    return int(move)


# This function first checks if the space is empty and if it can make a move.
def chooseRandomMoveFromList(board, moveList):
    possibleMove = []
    for i in moveList:
        if isSpaceFree(board, i):
            possibleMove.append(i)

    # This tells the program that if the list isnt empty then it can make a move.
    if len(possibleMove) != 0:
        return random.choice(possibleMove)
    else:
        return None


# This funciton containts the code for the "AI" to "think" and make a decision
def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # This tells the program to pick a number from one to nine.
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        # Makes a copy of the list board so it doesnt modify the global value of the variable board.
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i

    # This counters tehe player's move by checking if the player can win on their next move and counter them.
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i
    # Checks the corners.
    # It will first try to take one of the couners.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
    # This checks the middle for a potential move.
    if isSpaceFree(board, 5):
        return 5
    # And at last the sides of the boards are analysed for a potential move.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


# Checks if the board is full also tied with the function responsible for identifying a draw.
def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


# Welcomes the palyer
print('Welcome to Tic-Tac-Toe!')

while True:
    theBoard = [' '] * 10
    # Lets the player to enter either X or O.
    playerLetter, computerLetter = inputPlayerLetter()
    # Inherits the function that decides what goes first.
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first!')
    # Keeps trackmof if the game is still being played or it has concluded.
    gameIsPlaying = True

    # This will loop throught the functions that are responsible for the computer and players moves.
    while gameIsPlaying:
        if turn == 'player':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print("You won the game!")
                # Checks if the game as ended with the player winning.
                gameIsPlaying = False
            else:
                # Reuses the function that is tells the program if the board is full to indicate
                # its a draw .
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("The game is a tie!")
                    break
                # If the conditions :player has won or draw has not been reached then the program will
                # loop again to the function that decides the computer's next move.
                else:
                    turn = 'computer'
        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print("The computer won!")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("The game is a tie!")
                    break
                else:
                    # If the conditions :player has won or draw has not been reached then the program will
                    # loop again to the function that allows the player to make a move.
                    turn = 'player'

    # Ask the user to enter yes or no to play again or to terminate the running
    # program.
    print("Do you want to play again? (yes or no)")
    if not input().lower().startswith('y'):
        break
