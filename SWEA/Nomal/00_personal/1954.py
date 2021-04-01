import sys
sys.stdin = open("1954_input.txt")

T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    rect = [[0] * N for _ in range(N)]
    number = 1
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    point_r = 0
    point_c = 0
    k = N
    rect[0][0] = number

    while 1:
        for i in range(k - 1):
            number += 1
            point_r += dr[0]
            point_c += dc[0]
            rect[point_r][point_c] = number
        for i in range(k - 1):
            number += 1
            point_r += dr[1]
            point_c += dc[1]
            rect[point_r][point_c] = number
        for i in range(k - 1):
            number += 1
            point_r += dr[2]
            point_c += dc[2]
            rect[point_r][point_c] = number
        for i in range(k - 2):
            number += 1
            point_r += dr[3]
            point_c += dc[3]
            rect[point_r][point_c] = number
        number += 1
        if number > N*N:
            break
        point_r += dr[0]
        point_c += dc[0]
        rect[point_r][point_c] = number
        k -= 2
    print(f'#{test_case}')
    for i in range(N):
        print(*rect[i])

# ///////////////////////////////////////////////////////////////////////////////////
