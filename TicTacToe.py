board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# 0 1 2
# 3 4 5
# 6 7 8

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
    print(board[0], "-", board[1], "-", board[2])
    print(board[3], "-", board[4], "-", board[5])
    print(board[6], "-", board[7], "-", board[8])
    move += 1
    position = int(input())
    board[position] = players[move % 2]

print(board[0], "-", board[1], "-", board[2])
print(board[3], "-", board[4], "-", board[5])
print(board[6], "-", board[7], "-", board[8])

if ifWin() == 2:
    print("draw")
elif move % 2 == 1:
    print("win player: 1")
else:
    print("win player: 2")
