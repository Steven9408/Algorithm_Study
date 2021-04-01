import sys
sys.stdin = open("1979_input.txt")

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    plane = []
    for i in range(N):
        plane += [list(map(int, input().split()))]
    res = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if cnt == K and plane[i][j] == 0:
                res += 1
            cnt = (cnt+plane[i][j])*plane[i][j]
            if cnt == K and j == N-1:
                res += 1

    for j in range(N):
        cnt = 0
        for i in range(N):
            if cnt == K and plane[i][j] == 0:
                res += 1
            cnt = (cnt+plane[i][j])*plane[i][j]
            if cnt == K and i == N-1:
                res += 1


    print('#{} {}'.format(tc, res))
