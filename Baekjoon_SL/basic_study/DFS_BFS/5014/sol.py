from collections import deque

def fun(a):
    return int(a) - 1

F, S, G, U, D = map(fun, input().split())
U += 1
D += 1

visited = [False for _ in range(F+1)]
visited[S] = True


if S == G:
    res = 0
else:
    res = -1
    q = deque()
    q.append((S,0))

    while q:
        now, cost = q.popleft()

        new = now - D
        if 0 <= new <= F and not visited[new]:
            if new == G:
                res = cost + 1
                break
            else:
                visited[new] = True
                q.append((new, cost + 1))
        new = now + U
        if 0 <= new <= F and not visited[new]:
            if new == G:
                res = cost + 1
                break
            else:
                visited[new] = True
                q.append((new, cost + 1))

if res == -1:
    print("use the stairs")
else:
    print(res)