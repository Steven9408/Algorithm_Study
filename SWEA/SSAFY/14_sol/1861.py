import sys
sys.stdin = open("1861_input.txt")

T = int(input())
def sol(i_s, j_s):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    cnt = 1

    while True:
        for k in range(4):
            i_n = i_s + dr[k]
            j_n = j_s + dc[k]
            if (0 <= i_n < N) and (0 <= j_n < N):
                if arr[i_n][j_n] - arr[i_s][j_s] == 1:
                    direc = k
                    break
        else:
            break
        i_s = i_s + dr[direc]
        j_s = j_s + dc[direc]
        cnt += 1
    return cnt



for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    res = -1
    res2 = arr[0][0]

    for i in range(N):
        for j in range(N):
            max_v = sol(i,j)
            if res < max_v:
                res = max_v
                res2 = arr[i][j]
            elif res == max_v and arr[i][j] < res2:
                res2 = arr[i][j]
    print('#{} {} {}'.format(tc,res2,res))








