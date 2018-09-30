# Game Functions
def print_board(board):
    for i, ele in enumerate(board):
        if i%3 == 0:
            print("")

        print(ele, end=" ")
    print("")


def ask_position(board, players, rounds, pos):
    player  = players[rounds%2]
    try:
        pos = int(input('Player {}s Please choose a number 1-9: '.format(player)))
    except ValueError:
        return ask_position(**data)

    if pos in board:
        return pos
    else:
        print('{} is not valided please choose another position'.format(pos))
    return ask_position(**data)


def mark_on(pos, players, board, rounds):
    marker = players[rounds%2]
    board[pos-1] = marker
    data['rounds'] = rounds + 1


def is_straight(board):
    b = board
    is_win_h = [
        len(set(b[0:3])),
        len(set(b[3:6])),
        len(set(b[6:9])),
    ]

    is_win_v = [
        len(set(b[0::3])),
        len(set(b[1::3])),
        len(set(b[2::3])),
    ]

    is_win_diag = [
        len(set(b[0::4])),
        len(set(b[2:8:2])),
    ]

    linear_index = {
        'h': [0, 3, 6],
        'v': [0, 1, 2],
        'd': [4, 4]
    }

    labels = ['h0', 'h1', 'h2', 'v0', 'v1', 'v2', 'd0', 'd1']
    wins_vector = is_win_h+is_win_v+is_win_diag 

    which_one = [i for i, v in enumerate(wins_vector) if v == 1]

    if len(which_one) > 0:
        label = labels[which_one[0]]
        player_index = linear_index[label[0]][int(label[1])]
        player = board[player_index]
        print("Winner is {} player".format(player))
        return True

    return False


def game_loops(data):
    while True:
        if data['rounds'] >= 10:
            print("=== The Game is DRAW ===")
            break

        print('round:', data['rounds'])
        data['pos'] = ask_position(**data)
        mark_on(**data)
        print_board(data['board'])
        print("")
        if is_straight(data['board']):
            print("==== End Game! ====")
            break   


if __name__ == '__main__':
    players = ['X', 'O']
    data = {
        'players': players,
        'rounds': 1,
        'board': list(range(1, 10)),
        'pos': 0
    }

    print('==== Game Init ===')
    print_board(data['board'])
    game_loops(data)
