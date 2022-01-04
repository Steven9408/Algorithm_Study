N = int(input())

a, b = map(int, input().split())
a -= 1
b -= 1

M = int(input())

plane = [[False for _ in range(N)] for _ in range(N)]
visited = [False for _ in range(N)]
res = -1

for i in range(M):
    s, e = map(int,input().split())
    plane[s-1][e-1] = True
    plane[e-1][s-1] = True

q = [[a,0]]
while q:
    now, cost = q.pop(0)
    visited[now] = True
    if now == b:
        res = cost

    for i in range(N):
        if plane[now][i] and not visited[i]:
            q.append([i,cost+1])

print(res)