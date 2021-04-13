




def solution(arr):
    answer = []
    N = len(arr)
    global res
    res = [0,0]
    def sol(arr1):
        global res
        N = len(arr1)

        if N == 2:
            sum_v = 0
            for i in range(N):
                for j in range(N):
                    sum_v += arr1[i][j]
            # if sum_v == 0:
            #     res[0] += 1
            # elif sum_v == N*N:
            #     res[1] += 1
            # else:
            res[1] += sum_v
            res[0] += N*N - sum_v

        else:
            for i in range(0, N, N//2):
                for j in range(0, N, N//2):
                    unity = 1
                    temp = arr1[i][j]
                    arr_new = []
                    for i_s in range(N//2):
                        temp2 = []
                        for j_s in range(N//2):
                            temp2 += [arr1[i+i_s][j+j_s]]
                            if temp != arr1[i+i_s][j+j_s]:
                                unity = 0
                        arr_new += [temp2]

                    if unity:
                        res[temp] += 1
                    else:
                        sol(arr_new)
    sum_v = 0
    for i in range(N):
        for j in range(N):
            sum_v += arr[i][j]
    if sum_v ==  N*N:
        res = [0,1]
    elif sum_v == 0:
        res = [1,0]
    else:
        sol(arr)
    return res


print(solution([[1,1],[1,1]]))