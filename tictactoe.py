"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None
z = range(3)


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def count(board):
    count_x, count_o = 0, 0
    for i in z:
        for j in z:
            if board[i][j] == X:
                count_x += 1
            elif board[i][j] == O:
                count_o += 1
    return count_x, count_o


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    last_spot = 9
    count_x, count_o = count(board)
    if count_o + count_x == EMPTY: 
        return X
    elif count_x > count_o and count_x + count_o != last_spot:
        return O
    elif count_x == count_o and count_x + count_o != last_spot:
        return X
    elif count_x + count_o == last_spot:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = []
    for i in z:
        for j in z:
            if board[i][j] == EMPTY:
                action.append((i, j))
    return action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    boardcopy = copy.deepcopy(board)
    
    try:  
        if not action in actions(board):
            raise Exception
        else:
            move = player(boardcopy)
            i, j = action[0], action[1]
            boardcopy[i][j] = move     
            return boardcopy
    except IndexError:
        print("Not valid")
    

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    verticals = []

    for row in board:
        if row.count(X) == 3:
            return X
        if row.count(O) == 3:
            return O
        
    for j in z:
        vertical = [row[j] for row in board]
        verticals.append(vertical)
    for j in verticals:
        if j.count(X) == 3:
            return X
        if j.count(O) == 3:
            return O

    if board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X
    if board[0][2] == X and board[1][1] == X and board[2][0] == X:
        return X

    if board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O    
    if board[0][2] == O and board[1][1] == O and board[2][0] == O:
        return O
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    empty_counter = 0
    for row in board:
        empty_counter += row.count(EMPTY)
    if empty_counter == 0 or winner(board) != EMPTY:
        return True
    elif winner(board):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        vInf = -math.inf
        move = set()
        for action in actions(board):
            v = min_value(result(board,action))
            if v > vInf:
                vInf = v
                move = action
    elif player(board) == O:
        vnInf = math.inf
        move = set()
        for action in actions(board):
            v = max_value(result(board,action))
            if v < vnInf:
                vnInf = v
                move = action
    return move


def max_value(board):
    if terminal(board): 
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    if terminal(board): 
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))   
    return v