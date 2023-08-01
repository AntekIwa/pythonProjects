from random import choice
#TODO: dodac randoma
minimax_array = []

for i in range(0, 10 ** 5): minimax_array.append(2)


def prtBoard(x):
    print(x[0], " | ", x[1], " | ", x[2])
    print("-------------")
    print(x[3], " | ", x[4], " | ", x[5])
    print("-------------")
    print(x[6], " | ", x[7], " | ", x[8])


def empty_squares(board):
    empty_idx = []
    for i in range(0, 9):
        if board[i] == 0: empty_idx.append(i)
    return empty_idx


def decode_number(board_number):
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    number = board_number
    i = 0
    while (number > 0):
        board[i] = number % 3
        number //= 3
        i += 1
    return board


def code_board(board):
    result = 0
    for i in range(0, 9):
        result += board[i] * (3 ** i)
    return result


def if_win(board):
    if board[0] == board[1] and board[1] == board[2] and board[0] != 0:
        if board[0] == 2:
            return 1
        else:
            return -1

    if board[3] == board[4] and board[4] == board[5] and board[3] != 0:
        if board[3] == 2:
            return 1
        else:
            return -1

    if board[6] == board[7] and board[7] == board[8] and board[6] != 0:
        if board[6] == 2:
            return 1
        else:
            return -1

    if board[0] == board[3] and board[3] == board[6] and board[0] != 0:
        if board[0] == 2:
            return 1
        else:
            return -1

    if board[2] == board[5] and board[5] == board[8] and board[2] != 0:
        if board[2] == 2:
            return 1
        else:
            return -1

    if board[1] == board[4] and board[4] == board[7] and board[1] != 0:
        if board[1] == 2:
            return 1
        else:
            return -1

    if board[0] == board[4] and board[0] == board[8] and board[0] != 0:
        if board[0] == 2:
            return 1
        else:
            return -1

    if board[2] == board[4] and board[2] == board[6] and board[2] != 0:
        if board[2] == 2:
            return 1
        else:
            return -1

    for i in range(0, 9):
        if board[i] == 0:
            return 2

    return 0


def generating_boards(board_number, move):
    if if_win(decode_number(board_number)) < 2:
        minimax_array[board_number] = if_win(decode_number(board_number)) - move
        return
    minimax_neighbours = []
    empty_idx = empty_squares(decode_number(board_number))
    for idx in empty_idx:
        if move % 2 == 0:
            u = board_number + 2 * (3 ** idx)
        else:
            u = board_number + (3 ** idx)
        if minimax_array[u] == 2: generating_boards(u, move + 1)
        minimax_neighbours.append(minimax_array[u])
    if move % 2 == 0:
        minimax_array[board_number] = max(minimax_neighbours)
    else:
        minimax_array[board_number] = min(minimax_neighbours)


def best_move(board_number, move):
    minimax_neighbours = []
    neighbours = []
    empty_idx = empty_squares(decode_number(board_number))
    for idx in empty_idx:
        if move % 2 == 0:
            u = board_number + 2 * (3 ** idx)
        else:
            u = board_number + (3 ** idx)
        minimax_neighbours.append(minimax_array[u])
        neighbours.append(u)
    if move % 2 == 0:
        return neighbours[minimax_neighbours.index(max(minimax_neighbours))]
    else:
        return neighbours[minimax_neighbours.index(min(minimax_neighbours))]


def game():
    move = 0;
    board = 0
    print("Choose who you want to be, 1 or 2")
    who = int(input())
    if who == 2:
        pos = int(input())
        board+=2*(3**pos)
        move+=1
        prtBoard(decode_number(board))
        print()
    while if_win(decode_number(board)) == 2:
        if move % 2 == who - 1:
            board = best_move(board, move)
        else:
            pos = int(input())
            board += who*(3 ** pos)
        prtBoard(decode_number(board))
        print()
        move += 1


generating_boards(0, 0)
game()
