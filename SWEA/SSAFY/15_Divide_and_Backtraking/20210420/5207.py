import sys
sys.stdin = open("5207_input.txt")

T = int(input())

def bin_search(l,r,m):
    cnt = 0
    res1 = 0
    while l <= r:
        mid = (l + r) // 2
        if m == arr[mid]:
            res1 += 1
            break
        elif m > arr[mid]:
            l = mid + 1
            if cnt == 1:
                return 0
            cnt = 1

        elif m < arr[mid]:
            r = mid - 1
            if cnt == -1:
                return 0
            cnt = -1
    return res1

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    arr2 = list(map(int, input().split()))

    res = 0
    for i in range(M):
        temp = bin_search(0,N-1,arr2[i])
        res += temp
    print('#{} {}'.format(tc,res))
