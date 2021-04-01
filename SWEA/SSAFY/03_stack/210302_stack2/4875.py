import sys
sys.stdin = open("4875_input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = []
    stack = []
    res = 0
    for i in range(N):
        maze += [list(map(int, ' '.join(input()).split()))]
        for j in range(N):
            if maze[i][j] == 2:
                start = [i, j]

    visited = [[0]*N for _ in range(N)]
    stack += [start]
    visited[start[0]][start[1]] = 1
    dr = [-1,0,1,0]
    dc = [0,1,0,-1]

    while stack:
        r,c = stack.pop()
        for k in range(4):
            r_new = r + dr[k]
            c_new = c + dc[k]
            if (0 <= r_new < N and 0 <= c_new < N) and visited[r_new][c_new] == 0:
                if maze[r_new][c_new] == 0:
                    stack += [[r_new, c_new]]
                    visited[r_new][c_new] = 1
                elif maze[r_new][c_new] == 3:
                    res = 1
                    break
        if res == 1:
            break
    print('#{} {}'.format(tc,res))


