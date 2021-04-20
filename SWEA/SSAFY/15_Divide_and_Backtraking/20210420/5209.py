import sys
sys.stdin = open("5209_input.txt")

T = int(input())

def dfs(idx,cost):
    global check, min_c
    if idx == N:
        if min_c > cost:
            min_c = cost
    else:
        for i in range(N):
            if not check[i]:
                new_cost = cost + arr[i][idx]
                if new_cost < min_c:
                    check[i] = 1
                    dfs(idx+1, new_cost)
                    check[i] = 0

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    check = [0]*N
    min_c = 99*15
    dfs(0,0)
    print('#{} {}'.format(tc,min_c))
