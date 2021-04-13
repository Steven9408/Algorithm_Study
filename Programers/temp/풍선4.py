def solution(a):
    N = len(a)
    arr = [0]*N
    left = a[0]
    right = a[N-1]
    for i in range(1,N-1):
        if a[i] < left:
            arr[i] = 1
            left = a[i]
        if a[N-i-1] < right:
            arr[N-i-1] = 1
            right = a[N-i-1]
    return sum(arr)+2


print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))