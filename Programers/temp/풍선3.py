def solution(a):
    N = len(a)
    res = 0

    for i in range(N):
        b_cnt = 0
        k = 0
        for j in range(0,i):
            if a[i] < a[j]:
                b_cnt += 1
            k += 1
        if k == b_cnt:
            res += 1
            continue
        b_cnt = 0
        k = 0
        for j in range(i+1,N):
            if a[i] < a[j]:
                b_cnt += 1
            k += 1
        if k == b_cnt:
            res += 1
            continue



    return res


print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))