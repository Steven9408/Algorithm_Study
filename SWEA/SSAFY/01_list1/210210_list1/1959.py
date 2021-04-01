import sys
sys.stdin = open("1959_input.txt")

def dot_comp(list1, list2, interval):
    res = 0
    list1 = [0]*interval+list(list1)
    for i in range(len(list1)):
        res += list1[i]*list2[i]
    return res


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N1,N2 = list(map(int, input().split()))
    numbers1 = list(map(int, input().split()))
    numbers2 = list(map(int, input().split()))
    res = []
    for i in range(abs(N1-N2)+1):
        if N1 < N2:
            res += [dot_comp(numbers1,numbers2,i)]
        else:
            res += [dot_comp(numbers2,numbers1,i)]
    max_num = res[0]
    for i in range(len(res)):
        if res[i] > max_num:
            max_num = res[i]
    print(f'#{test_case} {max_num}')