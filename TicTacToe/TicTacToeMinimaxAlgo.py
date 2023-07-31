from random import choice
plansze = []
status = []
graph = []
moves = ['X', 'O']
cnt = 0


def prtBoard(x):
    print(x[0], " | ", x[1], " | ", x[2])
    print("-------------")
    print(x[3], " | ", x[4], " | ", x[5])
    print("-------------")
    print(x[6], " | ", x[7], " | ", x[8])


for i in range(0, 10 ** 6):
    graph.append([])
    plansze.append([])
    status.append(0)


def dfs(node, ruch):
    if ifWin(plansze[node]) < 3:
        status[node] = ifWin(plansze[node])
        return
    statusTmp = []
    for u in graph[node]:
        dfs(u,ruch+1)
        statusTmp.append(status[u])
    if ruch%2 == 1:
        status[node] = statusTmp[0]
        for i in range (1, len(statusTmp)):
            status[node] = min(status[node], statusTmp[i])
    else:
        status[node] = statusTmp[0]
        for i in range(1, len(statusTmp)):
            status[node] = max(status[node], statusTmp[i])


def ifWin(board):
    if board[0] == board[1] and board[1] == board[2]:
        if board[0] == 'O':
            return -1
        elif board[0] == 'X':
            return 1
    if board[3] == board[4] and board[4] == board[5]:
        if board[3] == 'O':
            return -1
        elif board[3] == 'X':
            return 1
    if board[6] == board[7] and board[7] == board[8]:
        if board[6] == 'O':
            return -1
        elif board[6] == 'X':
            return 1
    if board[0] == board[3] and board[3] == board[6]:
        if board[0] == 'O':
            return -1
        elif board[0] == 'X':
            return 1
    if board[2] == board[5] and board[5] == board[8]:
        if board[2] == 'O':
            return -1
        elif board[2] == 'X':
            return 1
    if board[1] == board[4] and board[4] == board[7]:
        if board[1] == 'O':
            return -1
        elif board[1] == 'X':
            return 1
    if board[0] == board[4] and board[0] == board[8]:
        if board[0] == 'O':
            return -1
        elif board[0] == 'X':
            return 1
    if board[2] == board[4] and board[2] == board[6]:
        if board[2] == 'O':
            return -1
        elif board[2] == 'X':
            return 1

    for i in range(0, 9):
        if board[i] == ' ':
            return 3
    return 0


def gen(numer, ruch, board):
    plansze[numer] = board.copy()
    if ifWin(plansze[numer]) < 3: return
    for i in range(0, 9):
        if board[i] == ' ':
            board[i] = moves[ruch % 2]
            global cnt
            cnt += 1
            graph[numer].append(cnt)
            gen(cnt, ruch + 1, board)
            board[i] = ' '


def gameMove(numer):
    statusTmp = []
    sasiedzi = []
    for u in graph[numer]:
        statusTmp.append(status[u])
        sasiedzi.append(u)
    maks = statusTmp[0]
    maksw = sasiedzi[0]
    for i in range (1, len(statusTmp)):
        if maks < statusTmp[i]:
            maks = statusTmp[i]
            maksw = sasiedzi[i]
    return maksw


def game():
    planszaAkt = plansze[0].copy()
    ruch = 0
    while (ifWin(planszaAkt) == 3):
        print(status[plansze.index(planszaAkt)], plansze.index(planszaAkt))
        prtBoard(planszaAkt)
        print(" ")
        print(" ")
        print(" ")
        if ruch == 0:
            planszaAkt[choice([0, 2, 6, 8])] = 'X'
        elif ruch % 2 == 0:
            planszaAkt = plansze[gameMove(plansze.index(planszaAkt))].copy()
        else:
            poz = int(input())
            planszaAkt[poz] = moves[1]

        ruch += 1
    prtBoard(planszaAkt)
    print(status[plansze.index(planszaAkt)])


gen(0, 0, [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
dfs(0,0)
game()
