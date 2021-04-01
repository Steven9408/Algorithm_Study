
import sys
sys.stdin = open("6485_input.txt")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    AB = []
    p = []

    for i in range(N):
        AB += [list(map(int, input().split()))]
    for i in range(int(input())):
        p += [int(input())]
    res = [0] * (len(p))
    for i in range(len(AB)):
        for j in range(len(p)):
            if AB[i][0] <= p[j] and AB[i][1] >= p[j] :
                res[j] += 1

    print(f'#{test_case}', end = ' ')
    print(*res)