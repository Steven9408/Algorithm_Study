import sys
sys.stdin = open("section_sum_input.txt")

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    arry = list(map(int, input().split()))
    max_num = 1*M
    min_num = 10000*M
    for i in range(N-M+1):
        sum_number = 0
        for j in range(M):
            sum_number += arry[i+j]
        if sum_number > max_num:
            max_num = sum_number
        if sum_number < min_num:
            min_num = sum_number
    res = max_num - min_num

    print('#{} {}'.format(tc, res))