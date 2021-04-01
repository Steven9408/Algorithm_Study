import sys
sys.stdin = open("1859_input.txt")
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    res = 0
    start = 0
    while 1:
        max_num = numbers[start]
        max_index = start
        for i in range(start, N):
            if max_num <= numbers[i]:
                max_num = numbers[i]
                max_index = i
        sum_v = 0
        for i in range(start, max_index):
            sum_v += numbers[i]

        res += (max_index-start) * max_num - sum_v
        start = max_index + 1
        if start + 1 > N:
            break
    print('#{} {}'.format(test_case, res))
