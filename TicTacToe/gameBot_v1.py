plansze = []
pozycjeWygrane = []
graph = []
moves = ['X', 'O']
cnt = 0

for i in range(0, 10 ** 6):
    pozycjeWygrane.append([0, 0, 0])
    graph.append([])
    plansze.append([])

def dfs(node):
    wygrane = 0
    porazki = 0
    remisy = 0
    for neighbour in graph[node]:
        dfs(neighbour)
        if pozycjeWygrane[neighbour][0] == 1:
            wygrane += 1
        elif pozycjeWygrane[neighbour][1] == 1:
            porazki += 1
        elif pozycjeWygrane[neighbour][2] == 1:
            remisy += 1
    if wygrane > 0:
        if porazki > 0:
            if remisy > 0:
                pozycjeWygrane[node][0] = 1
                pozycjeWygrane[node][1] = 1
                pozycjeWygrane[node][2] = 1
            else:
                pozycjeWygrane[node][0] = 1
                pozycjeWygrane[node][1] = 1
        else:
            if remisy > 0:
                pozycjeWygrane[node][0] = 1
                pozycjeWygrane[node][2] = 1

            else:
                pozycjeWygrane[node][0] = 1
    else:
        if porazki > 0:
            if remisy == 0:
                pozycjeWygrane[node][1] = 1
            else:
                pozycjeWygrane[node][1] = 1
                pozycjeWygrane[node][2] = 1
        else:
            if remisy > 0:
                pozycjeWygrane[node][2] = 1


def prtBoard(x):
    print(x[0], " | ", x[1], " | ", x[2])
    print("-------------")
    print(x[3], " | ", x[4], " | ", x[5])
    print("-------------")
    print(x[6], " | ", x[7], " | ", x[8])


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

def gen(numer, ruch, board):
    plansze[numer] = board.copy()
    if ifWin(plansze[numer]) == 0:
        if(ruch-1)%2 == 0:
            pozycjeWygrane[numer][0] = 1
        else:
            pozycjeWygrane[numer][1] = 1
        return
    if ifWin(plansze[numer]) == 2:
        pozycjeWygrane[numer][2] = 1
        return
    for i in range(0, 9):
        if board[i] == ' ':
            board[i] = moves[ruch % 2]
            global cnt
            cnt += 1
            graph[numer].append(cnt)
            gen(cnt, ruch + 1, board)
            board[i] = ' '

def gameMove(numer):
    # TODO: return lista.index(lista.max())
    # 0 - wygrana | 1 - przegrana | 2 - remis | 3 - remis/wygrana | 4 - remis/porazka | 5 - porazka/wygrana | 6 - porazka/wygrana/remis
    for s in graph[numer]:
        if pozycjeWygrane[s][0] == 1:
            return s
    for s in graph[numer]:
        if pozycjeWygrane[s][2] == 1:
            return s
    return graph[numer][0]

def game():
    planszaAkt = plansze[0].copy()
    ruch = 0
    while (ifWin(planszaAkt) == 1):
        prtBoard(planszaAkt)
        print(" ")
        print(" ")
        print(" ")
        if (ruch % 2 == 0):
            planszaAkt = plansze[gameMove(plansze.index(planszaAkt))].copy()
        else:
            poz = int(input())
            planszaAkt[poz] = moves[1]
        ruch += 1
    prtBoard(planszaAkt)

gen(0, 0, [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
dfs(0)
game()
