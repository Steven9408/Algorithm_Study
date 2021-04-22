import sys
sys.stdin = open("5250_input.txt")

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    INF = 99999


    arr = [list(map(int, input().split())) for _ in range(N)]

    w = [[INF]*N for _ in range(N)]

    temp = arr[1][0] - arr[0][0]
    if temp > 0:
        w[1][0] = temp + 1
    else:
        w[1][0] = 1
    temp = arr[0][1] - arr[0][0]
    if temp > 0:
        w[0][1] = temp + 1
    else:
        w[0][1] = 1
    U = {(0,0)}
    i_max = 1
    j_max = 1

    while len(U) != N*N:
        min_w = INF
        min_i = (-1,-1)
        for i in range(i_max+1):
            for j in range(j_max+1):
                if (i,j) not in U and w[i][j] < min_w:
                    min_i = (i,j)
                    min_w = w[i][j]
        U.add(min_i)
        now_i = min_i[0]
        now_j = min_i[1]
        dr = [-1,1,0,0]
        dc = [0,0,-1,1]
        cri = w[now_i][now_j]
        for k in range(4):
            temp_i = now_i + dr[k]
            temp_j = now_j + dc[k]

            if 0 <= temp_i < N and 0 <= temp_j < N and (temp_i,temp_j) not in U:
                value = arr[temp_i][temp_j] - arr[now_i][now_j]
                if value > 0:
                    tmp = cri + value + 1
                else:
                    tmp = cri + 1
                if tmp < w[temp_i][temp_j]:
                    w[temp_i][temp_j] = tmp
                if i_max < temp_i:
                    i_max = temp_i
                if j_max < temp_j:
                    j_max = temp_j

    print('#{} {}'.format(tc,w[N-1][N-1]))













