def solution(routes):
    N = len(routes)

    end = max(routes, key=lambda x:x[1])[1]
    start = min(routes, key=lambda x:x[0])[0]
    for i in range(N):
        routes[i][0] -= start
        routes[i][1] -= start
    N_r = end - start + 1
    arr = [[] for _ in range(N_r)]

    for i in range(N):
        for j in range(routes[i][0],routes[i][1]+1):
            arr[j] += [i]

    answer = 0
    while True:
        max_v = len(arr[0])
        max_i = 0
        len_list = []
        k = 0
        for i in range(N_r):
            len_list += [len(arr[i])]
            if max_v < len(arr[i]):
                max_i = i
                max_v = len(arr[max_i])
            if len_list[i] == 0:
                k += 1
        if k == N_r:
            break
        answer += 1
        max_car = list(arr[max_i])

        for i in max_car:
            for j in range(routes[i][0],routes[i][1]+1):
                len_list[j] -= 1
                arr[j].remove(i)

    return answer



print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))