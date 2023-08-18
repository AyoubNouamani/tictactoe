"""
Tic Tac Toe Player
"""

from math import inf as infinity 

import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


"""
Returns player who has the next turn on a board.
"""

def player(board):
    if board is None: raise Exception("[Player]: board is null")

    cmptX = 0
    cmptO = 0

    height = len(board)
    width = len(board[0])

    for i in range(0, height):
        for j in range(0, width):
            case = board[i][j];
            if (case == X): cmptX+=1
            elif (case == O): cmptO+=1
    
    if (cmptX == cmptO) : 
        return X
    else: 
        return O 


"""
Returns set of all possible actions (i, j) available on the board.
"""

def actions(board):
    if board is None: raise Exception("[Actions]: board is null")

    possibleMoves = set()
    height = len(board)
    width = len(board[0])

    for i in range(0, height):
        for j in range(0, width):
            if (board[i][j] == EMPTY):
                possibleMoves.add((i,j))
    return possibleMoves


def result(board, action):
    if (board is None): raise Exception("[Result]: board is None")
    if (action is None): raise Exception("[Result]: action is None")

    possibleMoves = actions(board)
    if not(action in possibleMoves):
        raise Exception("[Result]: action is invalid")

    board_cp = copy.deepcopy(board)
    turn = player(board)

    pos_h = action[0]
    pos_w = action[1]

    board_cp[pos_h][pos_w] = turn

    return board_cp


"""
Returns the winner of the game, if there is one.
"""

def winner(board):
    if (board is None): raise Exception("[Winner]: board is None")

    height = len(board)
    width = len(board[0])

    for i in range (0, height, 1):
        if (board[i][0] == board[i][1] == board[i][2]):
            return board[i][0]
        
    for i in range (0, width, 1):
        if (board[0][i] == board[1][i] == board[2][i]):
            return board[0][i]

    if (board[0][0] == board[1][1] == board[2][2]):
        return board[0][0]
    
    if (board[0][2] == board[1][1] == board[2][0]):
        return board[0][2]
    
    return None
    

"""
Returns True if game is over, False otherwise.
"""

def terminal(board):
    if (board is None): raise Exception("[Terminal]: board is None")

    if (winner(board) is None):
        for row in board:
            if EMPTY in row:
                return False
    
    return True


"""
Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
"""

def utility(board):
    if (board is None): raise Exception("[Utility]: board is None")
    
    state = winner(board)

    if (state == X): return 1
    if (state == 0): return -1
    
    return 0
    

"""
Returns the optimal action for the current player on the board.
"""

def minimax(board):
    if (board is None): raise Exception("[Minimax]: board is None")

    if terminal(board): 
       return None

    if player(board) == X:
        action_list = actions(board)
        if (len(action_list) == 9): return (0,0)
        best_val = -infinity
        best_move = None
        for action in action_list:
            move_val = min_val(result(board, action))
            if move_val > best_val:
                best_val = move_val
                best_move = action
        return best_move
    
    if player(board) == O:
        best_val = infinity
        best_move = None
        for action in actions(board):
            move_val = max_val(result(board, action))
            if move_val < best_val:
                best_val = move_val
                best_move = action
        return best_move
    
    raise Exception("Out of minmax")

def max_val(board):
    if terminal(board): 
        return utility(board)
    v = - infinity
    for action in actions(board):
        v = max(v, min_val(result(board, action)))
    return v


def min_val(board):
    if terminal(board): 
        return utility(board)
    v = infinity
    for action in actions(board):
        v = min(v, max_val(result(board, action)))
    return v

