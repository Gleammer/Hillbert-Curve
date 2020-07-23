import numpy as np


# Prints a MxN array
def print_matrix(board):
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            print(board[i][j], end=' ')
        print()


# Returns the transpose of a Matrix
def t_flip(board):
    return board.transpose()


# Returns the up-down flipped matrix
def ud_flip(board):
    return np.flip(board, 0)


# Return the left-right flipped matrix
def lr_flip(board):
    return np.flip(board, 1)


# Creates the next-level Hillbert matrix
def hill(board):
    temp1 = np.concatenate((t_flip(board), lr_flip(t_flip(board))), 1)
    temp2 = np.concatenate((board, board), 1)
    rez = np.concatenate((temp1, temp2), 0)
    return rez