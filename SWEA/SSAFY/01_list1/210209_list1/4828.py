import sys

sys.stdin = open("min_max_input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arry = list(map(int, input().split()))

    max_num = 1
    min_num = 1000000

    for i in range(N):
        if arry[i] > max_num:
            max_num = arry[i]
        if arry[i] < min_num:
            min_num = arry[i]

    res = max_num - min_num
    print('#{} {}'.format(tc, res))