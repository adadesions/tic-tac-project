import numpy as np
import time

def board_generator():
    board = np.round(np.random.random((4, 4))*100)
    board = board.astype(int)

    return board


def print_board(board):
    for row in board:
        for ele in row:
            print(ele, end='\t')
        print('')


def annouce_number():
    rand = np.random.randint(1, 100)
    print('The number is {} !!!'.format(rand))

    return rand

def mark_on(rand_num, board):
    if rand_num in board:
        print(board[board == rand_num])
        board[board == rand_num ] = -1
        print('Found', rand_num)
    else:
        print('Not found', rand_num)


def game_loop(data):
    board = data['board']
    while True:
        rand_num = annouce_number()
        mark_on(rand_num, board)
        print_board(board)
        time.sleep(0.5)


if __name__ == '__main__':
    data = {
        'board': board_generator()
    }
    np.random.seed(1)

    print_board(data['board'])
    game_loop(data)
