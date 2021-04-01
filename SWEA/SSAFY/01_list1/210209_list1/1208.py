import sys
sys.stdin = open("1208_input.txt")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    arry = list(map(int, input().split()))

    for i in range(N):
        max_num = arry[0]
        min_num = arry[0]
        max_idex = 0
        min_idex = 0

        for j in range(len(arry)):
            if arry[j] >= max_num:
                max_num = arry[j]
                max_index = j
            if arry[j] <= min_num:
                min_num = arry[j]
                min_index = j
        if max_num == min_num:
            break
        arry[max_index] += -1
        arry[min_index] += 1

        max_num = arry[0]
        min_num = arry[0]
        max_index = 0
        min_index = 0
        for j in range(len(arry)):
            if arry[j] >= max_num:
                max_num = arry[j]
                max_index = j
            if arry[j] <= min_num:
                min_num = arry[j]
                min_index = j
        res = max_num - min_num
    print(f'#{test_case} {res}')
