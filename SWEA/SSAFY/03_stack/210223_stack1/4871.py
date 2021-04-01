import sys
sys.stdin = open("4871_input.txt")

T = int(input())

for tc in range(1,T+1):
    V,E = list(map(int, input().split()))
    adj = [[0]*(V+1) for _ in range(V+1)]
    res = 0
    for i in range(E):
        s, e = list(map(int, input().split()))
        adj[s][e] = 1

    start, end = list(map(int, input().split()))

    stack = [start]
    # for i in range(1,V+1):
    #     print(adj[i])

    while stack:
        top = stack.pop()
        if top == end:
            res = 1
            break
        for i in range(1, V + 1):
            if adj[top][i] == 1:
                stack.append(i)
    print('#{} {}'.format(tc,res))



