import sys
sys.stdin = open("1226_input.txt")

T = 10

for tc in range(1,T+1):
    input()
    N = 16
    plane = []

    for i in range(N):
        plane += [list(map(int, ' '.join(input()).split()))]
        for j in range(N):
            if plane[i][j] == 2:
                r = i
                c = j
    check = [[0]*N for _ in range(N)]
    check[r][c] = 1
    dr = [-1,0,1,0]
    dc = [0,1,0,-1]
    stack = [[r,c]]
    res = 0

    while stack:
        r,c = stack.pop()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and plane[nr][nc] != 1 and check[nr][nc] == 0:
                if plane[nr][nc] == 3:
                    res = 1
                    break
                stack.append([nr,nc])
                check[nr][nc] = 1
        if res:
            break
    print('#{} {}'.format(tc,res))





