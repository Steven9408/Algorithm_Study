from collections import deque
t = int(input())
inter = 50


for _ in range(t):
    n = int(input())
    s_x, s_y = map(int, input().split())
    cs = []
    for j in range(n):
        cs.append(list(map(int, input().split())))
    e_x, e_y = map(int, input().split())

    visited = [False for _ in range(n)]
    q = deque([[s_x, s_y, 20]])
    res = 0

    while q:
        now_x, now_y, now_b = q.popleft()
        # 현재 위치에서 목적지 까지 갈 수 있는지 확인
        if abs(e_x-now_x) + abs(e_y-now_y) <= now_b*inter:
            res = 1
            break

        # 갈 수 있는 편의점을 찾자
        for i in range(len(cs)):
            if not visited[i]:
                c_x = cs[i][0]
                c_y = cs[i][1]
                if abs(c_x-now_x) + abs(c_y-now_y) <= now_b*inter:
                    q.append([c_x, c_y, 20])
                    visited[i] = True
    if res:
        print("happy")
    else:
        print("sad")
