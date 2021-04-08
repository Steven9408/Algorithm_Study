def solution(n, costs):
    def con(idex):
        global check
        global res
        if idex >= N:
            pass
            # 다 연결 되어 있는지 판별
            global check
            check = [0] * n
            find_route(0)
            print(check)
            # print(select)

            # 코스트 계산
            cnt = 0
            for i in range(N):
                if select[i] == 1:
                   cnt += costs[i][2]

        else:
            select[idex] = 0
            con(idex + 1)
            select[idex] = 1
            con(idex + 1)
    def find_route(idx):
        global check
        temp = []
        for i in range(N):
            if select[i] == 1 and costs[i][0] == idx and check[costs[i][1]] == 0:
                temp += [costs[i][1]]
            elif select[i] == 1 and costs[i][1] == idx and check[costs[i][0]] == 0:
                temp += [costs[i][0]]
        if temp:
            for i in range(len(temp)):
                check[temp[i]] = 1
                find_route(temp[i])
        else:
            return

    N = len(costs)
    select = [0] * N
    global res
    res = []

    con(0)

    answer = 0
    return answer

print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))