N, M, V = map(int, input().split())

visited = [False for _ in range(N)]

vector = [[False for _ in range(N)] for _ in range(N)]

for i in range(M):
    s,e = map(int, input().split())
    vector[s-1][e-1] = True
    vector[e-1][s-1] = True
# dfs
res = []
stack = [V-1]
while(stack):
    now = stack.pop(-1)
    if not visited[now]:
        visited[now] = True
        res.append(now+1)
        for i in range(N-1,-1,-1):
            if vector[now][i] and not visited[i]:
                stack.append(i)

print(*res)

# bfs
visited = [False for _ in range(N)]
res = []
queue = [V-1]
while(queue):
    now = queue.pop(0)
    if not visited[now]:
        visited[now] = True
        res.append(now+1)
        for i in range(N):
            if vector[now][i] and not visited[i]:
                queue.append(i)
print(*res)