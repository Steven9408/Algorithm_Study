
# x < M 일 때, x' = x + 1
# 아니면 x' = 1
# 결론 x_max = M
# 결론 y_max = N

K = int(input())

for t in range(K):
    M, N, x_n, y_n = map(int, input().split())

    cnt = 1
    x, y = 1, 1

    while True:
        cnt += 1
        if x < M:
            x += 1
        else:
            x = 1
        if y < N:
            y += 1
        else:
            y = 1

        if x == x_n and y == y_n:
            break
        if x == M and y == N:
            cnt = -1
            break
    print(cnt)