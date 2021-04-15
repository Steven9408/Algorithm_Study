import sys
sys.stdin = open("5188_input.txt")

T = int(input())


def dfs(i,j,sum_v):
    global max_v
    dr = [0,1]
    dc = [1,0]
    if i == N-1 and j == N-1:
        if sum_v < max_v:
            max_v = sum_v

    else:
        for k in range(2):
            i_n = i + dr[k]
            j_n = j + dc[k]
            if i_n < N and j_n < N:
                if max_v > sum_v+arr[i_n][j_n]:
                    dfs(i_n,j_n,sum_v+arr[i_n][j_n])




for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    global max_v
    max_v = 13*(2*N-1)
    dfs(0,0,arr[0][0])

    print('#{} {}'.format(tc, max_v))
