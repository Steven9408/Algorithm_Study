from collections import deque
from copy import deepcopy

def add(now,select):

    if select == 0:
        for i in range(N):
            for j in range(N):
                if now[i][j] != 0:
                    for k in range(i+1,N):
                        if now[k][j] != 0:
                            if now[k][j] == now[i][j]:
                                now[i][j] += now[k][j]
                                now[k][j] = 0
                            break
    elif select == 1:
        # 아래 방향
        for i in range(N-1,-1,-1):
            for j in range(N):
                if now[i][j] != 0:
                    for k in range(i-1, -1, -1):
                        if now[k][j] != 0:
                            if now[k][j] == now[i][j]:
                                now[i][j] += now[k][j]
                                now[k][j] = 0
                            break
    elif select == 2:
        # 왼쪽
        for j in range(N):
            for i in range(N):
                if now[i][j] != 0:
                    for k in range(j+1, N):
                        if now[i][k] != 0:
                            if now[i][k] == now[i][j]:
                                now[i][j] += now[i][k]
                                now[i][k] = 0
                            break
    elif select == 3:
        # 오른쪽
        for j in range(N-1, -1, -1):
            for i in range(N):
                if now[i][j] != 0:
                    for k in range(j-1, -1, -1):
                        if now[i][k] != 0:
                            if now[i][k] == now[i][j]:
                                now[i][j] += now[i][k]
                                now[i][k] = 0
                            break
    return now


def move(now, select):
    if select == 0:
        for i in range(N):
            for j in range(N):
                if now[i][j] != 0:
                    r = i
                    while 0 <= r + dr[select] < N and now[r + dr[select]][j] == 0:
                        r += dr[select]
                    now[i][j] , now[r][j] = now[r][j], now[i][j]


    elif select == 1:
        # 아래 방향
        for i in range(N-1,-1,-1):
            for j in range(N):
                if now[i][j] != 0:
                    r = i
                    while 0 <= r + dr[select] < N and now[r + dr[select]][j] == 0:
                        r += dr[select]
                    now[i][j], now[r][j] = now[r][j], now[i][j]
    elif select == 2:
        # 왼쪽
        for j in range(N):
            for i in range(N):
                if now[i][j] != 0:
                    c = j
                    while 0 <= c + dc[select] < N and now[i][c + dc[select]] == 0:
                        c += dc[select]
                    now[i][j], now[i][c] = now[i][c], now[i][j]
    elif select == 3:
        # 오른쪽
        for j in range(N-1, -1, -1):
            for i in range(N):
                if now[i][j] != 0:
                    c = j
                    while 0 <= c + dc[select] < N and now[i][c + dc[select]] == 0:
                        c += dc[select]
                    now[i][j], now[i][c] = now[i][c], now[i][j]
    return now

def search(now):
    global max_v
    for i in range(N):
        for j in range(N):
            if now[i][j] > max_v:
                max_v = now[i][j]

N = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
plane = []
for i in range(N):
    plane.append(list(map(int, input().split())))

q = deque([[deepcopy(plane),0]])
max_v = 0
while q:
    now , cost = q.popleft()

    # 회전 방향 설정
    for c in range(4):
        temp = deepcopy(now)
        temp = add(temp, c)
        # 이동시키기
        temp = move(temp,c)
        if cost + 1 == 5:
            search(temp)
        # q에 넣어주기
        else:
            q.append([temp,cost+1])
print(max_v)