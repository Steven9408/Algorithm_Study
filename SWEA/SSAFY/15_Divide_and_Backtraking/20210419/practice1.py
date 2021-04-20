def quick_sort(arr, l, r):
    if l < r:
        s = partition(arr, l, r)
        quick_sort(arr, l, s-1)
        quick_sort(arr, s+1, r)


def partition(arr, l, r):
    p = arr[l]
    i, j = l+1 ,r
    while i <= j:
        while arr[i] <= p:
            i += 1
        while arr[j] > p:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[l], arr[j] = arr[j], arr[l]
    return j

# [11, 45, 23, 81, 28, 34]
# [1,1,1,1,1,0,0,0,0,0]

arr = [1,1,1,1,1,0,0,0,0,0]
print(quick_sort(arr, 0, len(arr)-1))
print(arr)
