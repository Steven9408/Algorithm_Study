import sys
sys.stdin = open("5205_input.txt")


def quick_sort(arr, start, end):
    if start < end:
        s = partition(arr, start, end)
        quick_sort(arr, start, s-1)
        quick_sort(arr, s+1, end)


def partition(arr, start, end):
    p = arr[start]
    i, j = start ,end
    while i <= j:
        while i<= j and arr[i] <= p:
            i += 1
        while arr[j] > p:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[start], arr[j] = arr[j], arr[start]
    return j

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    quick_sort(arr, 0, N-1)

    print('#{} {}'.format(tc, arr[N//2]))

