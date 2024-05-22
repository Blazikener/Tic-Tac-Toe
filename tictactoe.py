"""
Tic Tac Toe Player
"""

import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countX = 0
    countO = 0

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == X:
                countX+=1
            if board[row][col] == O:
                countO += 1

    if countX > countO:
        return 0
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = set()
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == EMPTY:
                action.add((row,col))

    return action 

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    first = player(board)
    comp = deepcopy(board)
    i, j = action
    if board[i][j] != None:
        raise Exception
    else:
        comp[i][j] = first
    return comp

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for y in range(3):
        if (board[y][0] == board[y][1] == board[y][2]) and (board[y][0] != EMPTY):
            return board[y][0]
        if (board[0][y] == board[1][y] == board[2][y]) and (board[0][y] != EMPTY):
            return board[0][y]
    if (board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0]) \
            and board[1][1] != EMPTY:
        return board[1][1]
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:  # check if there is a winner or not
        return True
    elif EMPTY not in board[0] and EMPTY not in board[1] and EMPTY not in board[2]:
        return True
    else:
        return False
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win_player = winner(board)

    if win_player == X:
        return 1
    elif win_player == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    def maxvalue(board):
        bestmove = ()
        if terminal(board):
            return utility(board), bestmove
        else:
            v = -5
            for action in actions(board):
                minval = minvalue(result(board, action))[0]
                if minval > v:
                    v = minval
                    bestmove = action
            return v, bestmove


    def minvalue(board):
        bestmove = ()
        if terminal(board):
            return utility(board), bestmove
        else:
            v = 5
            for action in actions(board):
                maxval = maxvalue(result(board, action))[0]
                if maxval < v:
                    v = maxval
                    bestmove = action
            return v, bestmove


    currentplayer = player(board)

    if terminal(board):
        return None

    if currentplayer == X:
        return maxvalue(board)[1]

    else:
        return minvalue(board)[1]
