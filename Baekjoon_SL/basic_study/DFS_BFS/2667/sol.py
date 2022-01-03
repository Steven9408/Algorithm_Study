N = int(input())
plane = [[] for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for i in range(N):
    temp = input()
    for j in range(N):
        plane[i].append(int(temp[j]))

res = []
cnt = 0
for i in range(N):
    for j in range(N):
        if plane[i][j] == 1 and not visited[i][j]:
            q = [[i,j]]
            tc = 0
            cnt += 1
            while q:
                now_r, now_c = q.pop()
                if visited[now_r][now_c] == 0:
                    visited[now_r][now_c] = True
                    tc += 1
                    for k in range(4):
                        temp_r = now_r + dr[k]
                        temp_c = now_c + dc[k]
                        if 0 <= temp_r < N and 0 <= temp_c < N and plane[temp_r][temp_c] == 1 and not visited[temp_r][temp_c]:
                            q.append([temp_r, temp_c])

            res.append(tc)

print(cnt)
res.sort()
for i in range(cnt):
    print(res[i])

