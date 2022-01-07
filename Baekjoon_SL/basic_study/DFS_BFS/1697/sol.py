from collections import deque
M = 100000

N, K = map(int, input().split())

q = deque()
q.append((N,0))

visited = [False for _ in range(M+1)]
visited[N] = True
res = 0

if N == K:
    print(0)
else:
    while q:
        now, cost = q.popleft()
        # +1
        new = now + 1
        if 0 <= new <= M and not visited[new]:
            if new == K:
                res = cost  + 1
                break
            else:
                visited[new] = True
                q.append((new, cost+1))
        new = now - 1
        if 0 <= new <= M and not visited[new]:
            if new == K:
                res = cost + 1
                break
            else:
                visited[new] = True
                q.append((new, cost+1))

        new = now * 2
        if 0 <= new <= M and not visited[new]:
            if new == K:
                res = cost + 1
                break
            else:
                visited[new] = True
                q.append((new, cost+1))

    print(res)
