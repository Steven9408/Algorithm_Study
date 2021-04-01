import sys
sys.stdin = open("1210_input.txt")

T = 10

for tc in range(1, T+1):
    ladder = []
    trash = int(input())
    N = 100
    for i in range(N):
        ladder += [list(map(int, input().split()))]

    dr = [-1,0,0]
    dc = [0,1,-1]
    dir = 0
    for start_i in range(N):
        if ladder[N-1][start_i] == 2:
            ladder[N - 1][start_i] = 1
            r = N-2
            c = start_i
            while r > 0:
                if c == 0:
                    left = 0
                    right = ladder[r][c + 1]
                elif c == N - 1:
                    left = ladder[r][c - 1]
                    right = 0
                else:
                    left = ladder[r][c - 1]
                    right = ladder[r][c + 1]

                lr = left + right
                ud = ladder[r - 1][c] + ladder[r + 1][c]

                if ud + lr == 3:
                    if dir == 0:
                        if left == 1:
                            dir = 2
                        else:
                            dir = 1
                    else:
                        dir = 0
                r = r + dr[dir]
                c = c + dc[dir]
            break
    print('#{} {}'.format(tc,c))




