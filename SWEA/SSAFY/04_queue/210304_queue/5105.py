import sys
sys.stdin = open("5105_input.txt")

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    plane = []

    for i in range(N):
        plane += [list(map(int, ' '.join(input()).split()))]
        for j in range(N):
            if plane[i][j] == 2:
                r = i
                c = j
    Q = []
    check = [[0]*N for _ in range(N)]
    check[r][c] = 1
    dr = [-1,0,1,0]
    dc = [0,1,0,-1]
    Q += [(r,c,0)]
    res = 0

    while Q:
        r, c, cost = Q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N and plane[nr][nc] != 1 and check[nr][nc] == 0:
                if plane[nr][nc] == 3:
                    res = cost
                    break
                Q += [(nr,nc,cost+1)]
                check[nr][nc] = 1
    print('#{} {}'.format(tc, res))


