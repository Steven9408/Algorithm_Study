import sys
from collections import deque
sys.stdin = open("5250_input.txt")

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    INF = 99999


    arr = [list(map(int, input().split())) for _ in range(N)]

    w = [[INF]*N for _ in range(N)]
    w[0][0] = 0

    q = deque([(0,0)])

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    while q:
        now = q.popleft()
        now_i = now[0]
        now_j = now[1]
        cri = w[now_i][now_j]
        for k in range(4):
            temp_i = now_i + dr[k]
            temp_j = now_j + dc[k]

            if 0 <= temp_i < N and 0 <= temp_j < N:
                value = arr[temp_i][temp_j] - arr[now_i][now_j]
                if value > 0:
                    tmp = cri + value + 1
                else:
                    tmp = cri + 1
                if tmp < w[temp_i][temp_j]:
                    w[temp_i][temp_j] = tmp
                    q.append((temp_i,temp_j))

    print('#{} {}'.format(tc,w[N-1][N-1]))
