def solution(a):
    N = len(a)

    # 먼저 요소의 갯수를 파악한다.
    max_a = max(a)
    cnt_list = [[i, 0] for i in range(max_a+1)]
    for i in range(N):
        cnt_list[a[i]][1] += 1
    cnt_list = sorted(cnt_list, key=lambda x : x[1], reverse=True)
    print(a)
    print(cnt_list)

    for i in range(max_a+1):
        b = list(a)
        if cnt_list[i][1] == 0:
            res = 0:
        j = 0
        while j < N:
            while cnt_list[i][0] not in [b[j],b[j+1]]:
                b.pop(j+1)



            j += 2




    answer = -1
    return answer


print(solution([5,2,3,3,5,3]))