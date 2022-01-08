from collections import deque

N, M = map(int,input().split())

plane = []

for i in range(N):
    temp_i = list(map(int, input().split()))
    plane.append(temp_i)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

t = 0
res = 1

while res == 1:
    t += 1
    temp = []

    for i in range(N):
        for j in range(M):
            if plane[i][j] != 0:
                cnt = 0
                for k in range(4):
                    new_x = i + dr[k]
                    new_y = j + dc[k]
                    if 0 <= new_x < N and 0 <= new_y < M and plane[new_x][new_y] == 0:
                        cnt += 1
                temp.append([i,j,cnt])

    start = []
    for x,y,cnt in temp:
        plane[x][y] -= cnt
        if plane[x][y] <= 0:
            plane[x][y] = 0
        else:
            start.append([x, y])

    if not start or len(start) == 1:
        break

    q = deque([[start[0][0],start[0][1]]])
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[start[0][0]][start[0][1]] = True
    while q:
        x,y = q.popleft()

        for k in range(4):
            n_x = x + dr[k]
            n_y = y + dc[k]
            if 0 <= n_x < N and 0 <= n_y < M and not visited[n_x][n_y] and plane[n_x][n_y] != 0:
                visited[n_x][n_y] = True
                q.append([n_x,n_y])

    for x,y in start:
        if not visited[x][y]:
            res = 2
            break

if res == 2:
    print(t)
else:
    print(0)

