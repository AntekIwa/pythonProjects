board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# 0 1 2
# 3 4 5
# 6 7 8

def prtBoard():
    print(board[0], " | ", board[1], " | ", board[2])
    print("-------------")
    print(board[3], " | ", board[4], " | ", board[5])
    print("-------------")
    print(board[6], " | ", board[7], " | ", board[8])

def getMove():
    position = int(input())
    ds = 0
    while (ds == 0):
        if (position < 0 or position > 8):
            print("wartość spoza zakresu")
            position = int(input())
        elif (board[position] != ' '):
            print("pole zajęte")
            position = int(input())
        else:
            ds = 1
    return position

def ifWin():
    if (board[0] == board[1] and board[1] == board[2] and board[0] != ' ') or (board[3] == board[4] and board[4] == board[5] and board[3] != ' ') or (board[6] == board[7] and board[7] == board[8] and board[6] != ' '):
        return 0
    if (board[0] == board[3] and board[3] == board[6] and board[0] != ' ') or (board[1] == board[4] and board[4] == board[7] and board[1] != ' ') or (board[2] == board[5] and board[5] == board[8] and board[2] != ' '):
        return 0
    if (board[0] == board[4] and board[0] == board[8] and board[0] != ' ') or (board[2] == board[4] and board[2] == board[6] and board[2] != ' '):
        return 0
    for i in range(0, 9):
        if board[i] == ' ':

            return 1
    return 2


move = 0
players = ['O', 'X'];

while ifWin() == 1:
    prtBoard()
    move += 1
    board[getMove()] = players[move % 2]

prtBoard()

if ifWin() == 2:
    print("draw")
elif move % 2 == 1:
    print("win player: 1")
else:
    print("win player: 2")
