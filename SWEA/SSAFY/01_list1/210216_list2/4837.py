import sys
sys.stdin = open("4837_input.txt")

T = int(input())

for tc in range(1,T+1):
    N,K = map(int, input().split())
    M = 12
    numbers = list(range(1,13))
    res = 0
    for i in range(1<<M):
        cnt = 0
        sum_v = 0
        for j in range(len(numbers)):
            if i & (1<<j):
                cnt += 1
                sum_v += numbers[j]
        if cnt == N and sum_v == K:
            res += 1
    print('#{} {}'.format(tc,res))
