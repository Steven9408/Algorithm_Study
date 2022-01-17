res = -1
N, M = map(int, input().split())

arry = []
for i in range(N):
    temp = input()
    temp = list(temp)
    for j in range(M):
        if temp[j] == 'B':
            blue = (i,j)
        elif temp[j] == 'R':
            red = (i,j)
    arry.append(temp)

t = [[[[False for x1 in range(M)] for x2 in range(N)] for x3 in range(M)] for x4 in range(N)]
t[red[0]][red[1]][blue[0]][blue[1]] = True

# 시계방향 방향 벡터
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

q = []
q.append([list(red), list(blue), 0])

bp = False
while q:
    red_position, blue_position, lev = q.pop(0)

    if lev == 10:
        break
    # 네 방향 시도
    for i in range(4):
        blue_first = False

        # blue
        ball_cnt = 0
        nr, nc = list(blue_position)
        while arry[nr][nc] != '#':
            nr += dr[i]
            nc += dc[i]
            if red_position[0] == nr and red_position[1] == nc:
                ball_cnt += 1
            elif arry[nr][nc] == 'O':
                blue_first = True
                break

        if blue_first:
            continue
        n_blue_position = [nr - dr[i]*(1+ball_cnt), nc - dc[i]*(1+ball_cnt)]

        # red
        ball_cnt = 0
        nr, nc = list(red_position)
        while arry[nr][nc] != '#':
            nr += dr[i]
            nc += dc[i]
            if blue_position[0] == nr and blue_position[1] == nc:
                ball_cnt += 1
            elif arry[nr][nc] == 'O':
                if ball_cnt == 0:
                    res = lev + 1
                    bp = True
                    break
        if bp:
            break
        n_red_position = [nr-dr[i]*(1+ball_cnt),nc-dc[i]*(1+ball_cnt)]

        if t[n_red_position[0]][n_red_position[1]][n_blue_position[0]][n_blue_position[1]]:
            continue
        else:
            q.append([list(n_red_position),list(n_blue_position), lev+1])
            t[n_red_position[0]][n_red_position[1]][n_blue_position[0]][n_blue_position[1]] = True

    if bp:
        break

print(res)




