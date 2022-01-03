N,M = map(int, input().split())

plane = [[] for _ in range(N)]
for i in range(N):
    temp = input()
    for j in range(M):
        plane[i].append(int(temp[j]))

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
visited = [[False for _ in range(M)] for _ in range(N)]

res = -1
q = [[0,0,0]]

while q:
    now_r, now_c, cost = q.pop(0)
    if now_r == N-1 and now_c == M-1:
        res = cost + 1
        break

    if not visited[now_r][now_c] and plane[now_r][now_c] == 1:
        visited[now_r][now_c] = True
        for i in range(4):
            temp_r = now_r + dr[i]
            temp_c = now_c + dc[i]
            if 0 <= temp_r < N and 0 <= temp_c < M and not visited[temp_r][temp_c] and plane[temp_r][temp_c] == 1:
                q.append([temp_r, temp_c, cost+1])

print(res)