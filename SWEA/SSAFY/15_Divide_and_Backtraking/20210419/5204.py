import sys
sys.stdin = open("5204_input.txt")

T = int(input())


def merge_sort(start, end):
    global cnt1
    global arr
    N = end-start
    if N == 1:
        return
    merge_sort(start, start + N//2)
    merge_sort(start + N//2, end)

    res = []
    i = start
    j = start + N//2
    while i < start + N//2 and j < end:
        if arr[i] > arr[j]:
            res += [arr[j]]
            j += 1
        else:
            res += [arr[i]]
            i += 1

    if i < start + N//2:
        cnt1 += 1
        res += arr[i:start + N//2]
    else:
        res += arr[j:end]
    arr[start:end] = list(res)


for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt1 = 0
    merge_sort(0,N)
    print('#{} {} {}'.format(tc,arr[N//2],cnt1))

