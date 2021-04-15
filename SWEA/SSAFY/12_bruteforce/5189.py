import sys
sys.stdin = open("5189_input.txt")

T = int(input())
def dfs(k, now, sum_v):
    global min_v
    if k >= N:
        sum_v += arr[now][0]
        if sum_v < min_v:
            min_v = sum_v

    else:
        for i in range(N):
            if not check[i]:
                temp = sum_v + arr[now][i]
                if temp < min_v:
                    check[i] = 1
                    dfs(k+1, i, temp)
                    check[i] = 0

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_v = 100*N
    check = [0]*N
    check[0] = 1
    dfs(1, 0, 0)

    print('#{} {}'.format(tc, min_v))
