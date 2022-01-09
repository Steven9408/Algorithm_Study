N, M = map(int, input().split())


def cir(n, i):
    if i < 0:
        return n - i*(-1)
    else:
        return i

robot = list(map(int, input().split()))
plane = []
for i in range(N):
    plane.append(list(map(int, input().split())))

check = [[False for _ in range(M)] for _ in range(N)]
now = list(robot)

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
desti = True
while True:
    n_r = now[0]
    n_c = now[1]
    dir = now[2]
    # 현재 위치 청소
    if not check[n_r][n_c] and desti:
        check[n_r][n_c] = True

    # 왼쪽부터 인접 칸 탐색
    for i in range(1, 5):
        now_dir = cir(4, dir - i)
        r = n_r + dr[now_dir]
        c = n_c + dc[now_dir]
        # a
        if plane[r][c] == 0 and not check[r][c]:
            now = [r, c , now_dir]
            desti = True
            break
    else:
        now_dir = cir(4, dir - 2)
        r = n_r + dr[now_dir]
        c = n_c + dc[now_dir]
        if plane[r][c] == 0:
            desti = False
            now = [r, c, dir]
            continue
        else:
            break


cnt = 0
for i in range(N):
    for j in range(M):
        if check[i][j] == True:
            cnt += 1
print(cnt)