def solution(a):
    N = len(a)
    cnt = 0

    for i in range(N):
        left = 0
        right = 0
        for j in range(N):
            if a[i] < a[j]:
                if j < i :
                    left += 1
                else :
                    right += 1
        print(left, right)
        if N - left -right == 1:
            cnt += 1
            continue
        if i - left == 0 or i + right == N-1:
            cnt += 1
            continue
    answer = 0
    return cnt


print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))