#TODO: zrobic optymalne chodzenie po drzewie
#TODO: pocalowac antosia
plansze = []
pozycjeWygrane = []
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
    pozycjeWygrane.append([0, 0, 0])
    graph.append([])
    plansze.append([])
    status.append(0)

def dfs(node):
    wygrane = 0
    porazki = 0
    remisy = 0
    #gdy jestesmy w lisciu
    if ifWin(plansze[node]) == 0:
        pozycjeWygrane[node][0] = 1
        return
    if ifWin(plansze[node]) == -1:
        pozycjeWygrane[node][1] = 1
        return
    if ifWin(plansze[node]) == 2:
        pozycjeWygrane[node][2] = 1;
        return
    czyPorazka = False
    czyRemis = False
    czyWygrana = False
    #gdy mozna grac dalej
    for neighbour in graph[node]:
        dfs(neighbour)
        if ifWin(plansze[neighbour]) == 0:
            czyWygrana = True
        if ifWin(plansze[neighbour]) == -1:
            czyPorazka = True
        if ifWin(plansze[neighbour]) == 2:
            czyRemis = True
        if pozycjeWygrane[neighbour][0] == 1:
            wygrane += 1
        if pozycjeWygrane[neighbour][1] == 1:
            porazki += 1
        if pozycjeWygrane[neighbour][2] == 1:
            remisy += 1

    if czyWygrana:
        pozycjeWygrane[node][0] = 1
        return
    if czyRemis:
        pozycjeWygrane[node][2] = 1
        return
    if czyPorazka:
        pozycjeWygrane[node][1] = 1
        return
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



# 0 - wygrana X
# -1 - przegrana X


def ifWin(board):
    if board[0] == board[1] and board[1] == board[2]:
        if board[0] == 'O':
            return -1
        elif board[0] == 'X':
            return 0
    if board[3] == board[4] and board[4] == board[5]:
        if board[3] == 'O':
            return -1
        elif board[3] == 'X':
            return 0
    if board[6] == board[7] and board[7] == board[8]:
        if board[6] == 'O':
            return -1
        elif board[6] == 'X':
            return 0

    if board[0] == board[3] and board[3] == board[6]:
        if board[0] == 'O':
            return -1
        elif board[0] == 'X':
            return 0
    if board[2] == board[5] and board[5] == board[8]:
        if board[2] == 'O':
            return -1
        elif board[2] == 'X':
            return 0
    if board[1] == board[4] and board[4] == board[7]:
        if board[1] == 'O':
            return -1
        elif board[1] == 'X':
            return 0

    if board[0] == board[4] and board[0] == board[8]:
        if board[0] == 'O':
            return -1
        elif board[0] == 'X':
            return 0
    if board[2] == board[4] and board[2] == board[6]:
        if board[2] == 'O':
            return -1
        elif board[2] == 'X':
            return 0

    for i in range(0, 9):
        if board[i] == ' ':
            return 1
    return 2


def gen(numer, ruch, board):
    plansze[numer] = board.copy()
    if ifWin(plansze[numer]) != 1: return
    for i in range(0, 9):
        if board[i] == ' ':
            board[i] = moves[ruch % 2]
            global cnt
            cnt += 1
            graph[numer].append(cnt)
            gen(cnt, ruch + 1, board)
            board[i] = ' '


def gameMove(numer):
    # wygrana - wygrana/remis - remis - porazka/wygrana/remis - porazka/wygrana -   remis/porazka - porazka
    maks = 0
    maksw = 0
    for s in graph[numer]:
        if(status[s] > maks):
            maks = status[s]
            maksw = s
    return maksw
#0 - wygrane | 1 - porazki | 2 - remisy


def preproces():
    for i in range(0, 10**6):
        if(pozycjeWygrane[i][0] == 1 and pozycjeWygrane[i][1] == 0 and pozycjeWygrane[i][2] == 0): status[i] = 7;
        elif (pozycjeWygrane[i][0] == 1 and pozycjeWygrane[i][1] == 0 and pozycjeWygrane[i][2] == 1): status[i] = 6;
        elif (pozycjeWygrane[i][0] == 0 and pozycjeWygrane[i][1] == 0 and pozycjeWygrane[i][2] == 1): status[i] = 5;
        elif (pozycjeWygrane[i][0] == 1 and pozycjeWygrane[i][1] == 1 and pozycjeWygrane[i][2] == 0): status[i] = 4;
        elif (pozycjeWygrane[i][0] == 1 and pozycjeWygrane[i][1] == 1 and pozycjeWygrane[i][2] == 1): status[i] = 3;
        elif (pozycjeWygrane[i][0] == 0 and pozycjeWygrane[i][1] == 1 and pozycjeWygrane[i][2] == 1): status[i] = 2;
        else: status[i] = 1;


def game():
    planszaAkt = plansze[0].copy()
    ruch = 0
    while (ifWin(planszaAkt) == 1):
        print(status[plansze.index(planszaAkt)], plansze.index(planszaAkt))
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
    print(status[plansze.index(planszaAkt)])


#wygrana porazka remis


gen(0, 0, [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
dfs(0)
preproces()
game()
