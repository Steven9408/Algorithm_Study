# By BFS
N = int(input())
V = int(input())

vector = [[False for _ in range(N)] for _ in range(N)]
visited = [False for _ in range(N)]

for i in range(V):
    s, e = map(int, input().split())
    vector[s-1][e-1] = True
    vector[e-1][s-1] = True

q = [0]

while q:
    now = q.pop(0)

    if not visited[now]:
        visited[now] = True
        for i in range(N):
            if vector[now][i] and not visited[i]:
                q.append(i)

res = 0
for i in range(N):
    if visited[i]:
       res += 1

print(res-1)