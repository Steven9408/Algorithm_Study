def solution(a):
    N = len(a)
    sorted_arr = list(a)
    sorted_arr.sort(reverse=True)
    cnt = 0

    for i in range(N):
        arr1 = list(a)
        now_value = arr1[i]
        s_arr1 = list(sorted_arr)
        # 현재 자신보다 큰 값을 다 없앤다.
        k = s_arr1.pop(0)
        while k != now_value:
            arr1.remove(k)
            k = s_arr1.pop(0)

        if len(arr1) == 1:
            cnt += 1
            continue
        if arr1.index(now_value) == 0 or arr1.index(now_value) == len(arr1)-1:
            cnt += 1
            continue

    answer = 0
    return cnt


print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))