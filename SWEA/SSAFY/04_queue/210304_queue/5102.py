import sys
sys.stdin = open("5102_input.txt")

T = int(input())

for tc in range(1,T+1):
    V, E = map(int, input().split())

    adj = [[0]*(V+1) for _ in range(V+1)]

    for i in range(E):
        s, e = map(int, input().split())
        adj[s][e] = 1
        adj[e][s] = 1

    check = [0]*(V+1)
    Q = []
    S, G = map(int, input().split())
    Q.append([S,0])
    check[S] = 1
    res = 0

    while Q:
        now,cost = Q.pop(0)
        for i in range(V+1):
            if adj[now][i] and not check[i]:
                Q.append([i,cost+1])
                check[i] = 1
                if i == G:
                    res = cost+1
                    break
        if res:
            break
    print('#{} {}'.format(tc,res))