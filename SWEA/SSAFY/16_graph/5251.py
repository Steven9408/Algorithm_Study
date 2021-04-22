import sys
from collections import deque
sys.stdin = open("5251_input.txt")

T = int(input())


for tc in range(1, T+1):
    N,E = map(int, input().split())
    INF = 99999
    arr = [[INF]*(N+1) for _ in range(N+1)]
    for i in range(E):
        data = list(map(int, input().split()))
        arr[data[0]][data[1]] = data[2]

    w = [INF]*(N+1)
    w[0] = 0

    q = deque([0])
    while q:
        now = q.popleft()
        adj = list(arr[now])

        for i in range(N+1):
            if adj[i] != INF:
                tmp = w[now] + adj[i]
                if tmp < w[i]:
                    w[i] = tmp
                    q.append(i)
    print('#{} {}'.format(tc,w[N]))



