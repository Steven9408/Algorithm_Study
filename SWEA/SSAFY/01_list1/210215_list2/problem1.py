import sys
sys.stdin = open("problem1_input.txt")

T = 10
N = 100
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    max_sum = 0
    arry = []
    ttt = int(input())

    for i in range(N):
        now_sum = 0
        arry.append(list(map(int, input().split())))
        for j in range(N):
            now_sum += arry[i][j]
        if max_sum < now_sum:
            max_sum = now_sum

    for j in range(N):
        now_sum = 0
        for i in range(N):
            now_sum += arry[i][j]
        if max_sum < now_sum:
            max_sum = now_sum

    now_sum = 0
    now_sum1 = 0
    for i in range(N):
        now_sum += arry[i][i]
        now_sum1 += arry[i][N-1-i]
    if max_sum < now_sum:
        max_sum = now_sum
    if max_sum < now_sum1:
        max_sum = now_sum1

    print(f'#{test_case} {max_sum}')