import sys
sys.stdin = open("2814_input.txt")

def dfs(c,d):
    global max_length
    if max_length < d:
        max_length = d
    for i in range(0,N):
        if adj[c][i] and not check[i]:
            check[i] = 1
            dfs(i,d+1)
            check[i] = 0


T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())

    adj = [[0]*N for _ in range(N)]
    for i in range(M):
        s,e = map(int,input().split())
        adj[s-1][e-1] = 1
        adj[e-1][s-1] = 1
    check = [0]*N
    max_length = 0
    for i in range(0,N):
        check[i] = 1
        dfs(i,1)
        check[i] = 0
    print("#{} {}".format(tc,max_length))