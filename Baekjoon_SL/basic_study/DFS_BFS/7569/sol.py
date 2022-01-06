from collections import deque

M, N, H = map(int, input().split())

cube = [[[] for _ in range(N)] for _ in range(H)]

q = deque()
cnt_r = 0
cnt_e = 0
for k in range(H):
    for j in range(N):
        temp_a = list(map(int, input().split()))
        cube[k][j] = list(temp_a)
        for i in range(M):
            if temp_a[i] == 1:
                q.append([k,j,i,0])
                cnt_r += 1
            elif temp_a[i] == -1:
                cnt_e += 1

di = [-1, 0, 1, 0, 0, 0]
dj = [0, 1, 0, -1, 0, 0]
dk = [0, 0, 0, 0, -1, 1]

# 익은 토마토가 없으면 무조건 -1
if cnt_r == 0:
    print(-1)
# 다 익어 있으면 0
elif N*H*M - cnt_e == cnt_r:
    print(0)
else:
    while q:
        k1, j1, i1, cost = q.popleft()
        for c in range(6):
            k2 = k1 + dk[c]
            j2 = j1 + dj[c]
            i2 = i1 + di[c]
            if 0 <= i2 < M and 0 <= j2 < N and 0 <= k2 < H and cube[k2][j2][i2] == 0:
                cube[k2][j2][i2] = 1
                q.append([k2, j2, i2, cost+1])

    res = cost
    # 안익은게 있으면 -1
    for k in range(H):
        for j in range(N):
            for i in range(M):
                if cube[k][j][i] == 0:
                    res = -1
                    break
            if res == -1:
                break
        if res == -1:
            break

    print(res)