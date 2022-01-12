# N*N 크기에 사탕을 채워 놓는다.

# 사탕색은 모두 같지 않을 수 있다 > 같지 않거나 같을 수도 있다.

# 사탕색이 다른 인접한 두칸을 고른다.
# 그 다음 코른칸에 들어있는 사탕을 서로 교환한다.

# 이제, 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분을 고른 다음 그 사탕을 모두 먹는다.

# 사탕이 채워진 상태가 주여젔을 때, 상근이가 먹을 수 있는 사탕의 최대 개수를 구하시오.

# C,P,Z,Y의 색깔 총 4종
# 사탕 색이 다른 인접한 두 칸이 존재하는 입력만 주어진다.
N = int(input())

plane = []
for i in range(N):
    plane.append(list(''.join(input())))

dr = [1, 0]
dc = [0, 1]

res = 0
for i in range(N):
    for j in range(N):
        for k in range(2):
            n_r = i + dr[k]
            n_c = j + dc[k]
            if 0 <= n_r < N and 0 <= n_c < N and plane[i][j] != plane[n_r][n_c]:
                plane[i][j], plane[n_r][n_c] = plane[n_r][n_c], plane[i][j]

                max_v = 1
                for i1 in range(N):
                    cnt = 1
                    for j1 in range(1,N):
                        if plane[i1][j1-1] == plane[i1][j1]:
                            cnt += 1
                        else:
                            cnt = 1
                        if cnt > max_v:
                            max_v = cnt
                    cnt = 1
                    for j1 in range(1,N):
                        if plane[j1-1][i1] == plane[j1][i1]:
                            cnt += 1
                        else:
                            cnt = 1
                        if cnt > max_v:
                            max_v = cnt
                if res < max_v:
                    res = max_v
                plane[n_r][n_c], plane[i][j] = plane[i][j], plane[n_r][n_c]


print(res)

