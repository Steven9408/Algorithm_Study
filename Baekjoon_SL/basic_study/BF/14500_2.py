N, M = map(int, input().split())
arr = []
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
visited = []
max_v = 0
res = 0
def dfs(visited, l, v, r, c):
    global res, max_v
    if l == 4:
        if res < v:
            res = v
    elif ((4-l)*max_v + v) >= res:
        for k in range(4):
            n_r = r + dr[k]
            n_c = c + dc[k]
            if (0 <= n_r < N) and (0 <= n_c < M) and [n_r, n_c] not in visited:
                visited.append([n_r, n_c])
                dfs(visited, l+1, v+arr[n_r][n_c], n_r, n_c)
                visited.pop(-1)
        if l == 2:
            r1, c1, r2, c2 = r+dr[0], c+dc[0], r+dr[1], c+dc[1]
            if (0 <= r1 < N) and (0 <= r2 < N) and (0 <= c1 < M) and (0 <= c2 < M) and [r1, c1] not in visited and [r2, c2] not in visited:
                t_v1 = v + arr[r1][c1] + arr[r2][c2]
                res = max(t_v1, res)
            r1, c1, r2, c2 = r + dr[2], c + dc[2], r + dr[3], c + dc[3]
            if (0 <= r1 < N) and (0 <= r2 < N) and (0 <= c1 < M) and (0 <= c2 < M) and [r1, c1] not in visited and [r2, c2] not in visited:
                t_v2 = v + arr[r1][c1] + arr[r2][c2]
                res = max(t_v2, res)



for i in range(N):
    temp = list(map(int, input().split()))
    max_v = max(max_v, max(temp))
    arr.append(temp)

for i in range(N):
    for j in range(M):
        visited.append([i,j])
        dfs(visited, 1, arr[i][j], i, j)
        visited.pop(0)


print(res)