N, M, K = map(int, input().split())

plane = []
max_v = -10000
for i in range(N):
    temp = list(map(int, input().split()))
    max_v = max(max_v, max(temp))
    plane.append(temp)

visited = [[False for _ in range(M)] for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
res = -10000*N*M
def dfs(l, arr , v):
    global res
    if l == K:
        if res < v:
            res = v
    else:
        for i in range(N):
            for j in range(M):
                t = plane[i][j]
                if not visited[i][j] and (v+t + (K-l-1)*max_v) >= res:
                    cir = False
                    for k in range(l):
                        r,c = arr[k]
                        for d in range(4):
                            if i == r + dr[d] and j == c + dc[d]:
                                cir = True
                                break
                        if cir:
                            break
                    if not cir:
                        visited[i][j] = True
                        dfs(l+1, arr + [[i,j]], v+t)
                        visited[i][j] = False

dfs(0, [], 0)
print(res)

