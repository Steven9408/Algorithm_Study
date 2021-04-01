import sys
sys.stdin = open("1859_input.txt")



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n = int(input())
    numbers = list(map(int, input().split()))
    res = 0
    start = 0
    while 1:
        max_num = max(numbers[start:n])
        max_num = numbers[start]
        max_index = start
        for i in range(start,n):
            if max_num <= numbers[i]:
                max_num = numbers[i]
                max_index = i
        max_index = max_index-start
        sum_v = 0
        for i in range(start, max_index + start):
            sum_v += numbers[i]

        # res += (max_index) * max_num - sum(numbers[start:max_index + start])
        res += (max_index) * max_num - sum_v
        start = max_index + 1 + start
        if start + 1 > n:
            break

    print('#{} {}'.format(test_case, res))
