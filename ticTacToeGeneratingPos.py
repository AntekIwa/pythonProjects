plansze = []
pozycjeWygrane = []
#362 880
for i in range(0, 10**9):
    plansze.append([])
    pozycjeWygrane.append(0)
plansze[0] = [' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ']

#0 - przegrana | 1 - wygrana | 2 - remis

def prtBoard(board):
    print(board[0], " | ", board[1], " | ", board[2])
    print("-------------")
    print(board[3], " | ", board[4], " | ", board[5])
    print("-------------")
    print(board[6], " | ", board[7], " | ", board[8])


def ifWin(board):
    if (board[0] == board[1] and board[1] == board[2] and board[0] != ' ') or (
            board[3] == board[4] and board[4] == board[5] and board[3] != ' ') or (
            board[6] == board[7] and board[7] == board[8] and board[6] != ' '):
        return 0
    if (board[0] == board[3] and board[3] == board[6] and board[0] != ' ') or (
            board[1] == board[4] and board[4] == board[7] and board[1] != ' ') or (
            board[2] == board[5] and board[5] == board[8] and board[2] != ' '):
        return 0
    if (board[0] == board[4] and board[0] == board[8] and board[0] != ' ') or (
            board[2] == board[4] and board[2] == board[6] and board[2] != ' '):
        return 0
    for i in range(0, 9):
        if board[i] == ' ':
            return 1
    return 2

moves = ['X', 'O']

def gen(numer, ruch):
    print(numer)
    prtBoard(plansze[numer])
    print("- - - - - - - -- - - - -")
    if ifWin(plansze[numer]) == 0:
        pozycjeWygrane[numer] = ruch%2
        print("wygrana")
        return
    if ifWin(plansze[numer]) == 2:
        pozycjeWygrane[numer] = 2
        print("remis")
        return
    for i in range(0, 9):
        board = plansze[numer]
        if board[i] == ' ':
            board[i] = moves[ruch%2]
            plansze[(numer*9) + i + 1] = board
            gen((numer*9) + i + 1, ruch + 1)
            board[i] = ' '

gen(0, 0)
