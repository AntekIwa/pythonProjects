plansze = [[' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ']]
pozycjeWygrane = []
graph = []
#362 880
for i in range(0, 10**6):
    pozycjeWygrane.append(-1)
    graph.append([])
#0 - wygrana | 1 - przegrana | 2 - remis | 3 - remis/wygrana | 4 - remis/porazka | 5 - porazka/wygrana | 6 - porazka/wygrana/remis

def dfs(node):
    wygrane = 0
    porazki = 0
    remisy = 0
    for neighbour in graph[node]:
        dfs(neighbour)
        if pozycjeWygrane[neighbour] == 0: wygrane+=1
        elif pozycjeWygrane[neighbour] == 1: porazki+=1
        elif pozycjeWygrane[neighbour] == 2: remisy+=1

    if wygrane > 0:
        if porazki > 0:
            if remisy > 0:
               pozycjeWygrane[node] = 6
            else:
                pozycjeWygrane[node] = 5
        else:
            if remisy > 0:
                pozycjeWygrane[node] = 3
            else:
                pozycjeWygrane[node] = 0

    else:
        if porazki > 0:
            if remisy == 0:
                pozycjeWygrane[node] = 1
            else:
                pozycjeWygrane[node] = 4

        else:
            if remisy > 0:
                pozycjeWygrane[node] = 2


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
cnt = 0

def gen(numer, ruch):
    #print(numer)
    #prtBoard(plansze[numer])
    #print("- - - - - - - -- - - - -")
    if ifWin(plansze[numer]) == 0:
        pozycjeWygrane[numer] = (ruch-1)%2
       # print("wygrana")
        return
    if ifWin(plansze[numer]) == 2:
        pozycjeWygrane[numer] = 2
        #print("remis")
        return
    for i in range(0, 9):
        board = plansze[numer]
        if board[i] == ' ':
            global cnt
            graph[numer].append(cnt + 1)

            cnt += 1

            board[i] = moves[ruch%2]
            plansze.append(board)
            gen(cnt, ruch + 1)
            board[i] = ' '

#0 - wygrana | 1 - przegrana | 2 - remis | 3 - remis/wygrana | 4 - remis/porazka | 5 - porazka/wygrana | 6 - porazka/wygrana/remis
gen(0, 0)
dfs(0)
print("porazki: ", pozycjeWygrane.count(1))
print("wygrane: ", pozycjeWygrane.count(0))
print("remisy: ", pozycjeWygrane.count(2))
print("wygrane/remisy: ", pozycjeWygrane.count(3))
print("wygrane/porazki: ", pozycjeWygrane.count(5))
print("remisy/porazki: ", pozycjeWygrane.count(4))
print("remisy/porazki/wygrane: ", pozycjeWygrane.count(6))
print("lacznie mozliwosci: ", pozycjeWygrane.count(1) + pozycjeWygrane.count(0) + pozycjeWygrane.count(2))
#255,168
