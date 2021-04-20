def solution(a, edges):
    N = len(a)
    M = N-1
    many = [0]*N
    k = 0
    if sum(a):
        return -1
    cnt = 0
    for i in range(N):
        if a[i] != 0:
            cnt += 1
    if cnt == 0:
        return 0

    infor = []

    for i in range(N):
        temp = []
        for j in range(M):
            if edges[j][0] == i:
              temp.append(edges[j][1])
            elif edges[j][1] == i:
              temp.append(edges[j][0])
        infor += [temp]



    while True:
        M = len(edges)
        many = [0] * N


        # 간선이 하나인 노드의 인덱스 추출
        one_way = []
        for i in range(N):
            if len(infor[i]) == 1 and infor[i][0] != -1:
                one_way += [i]

        # 간선이 하나인 노드를 부모에게 더해주고, 해당간선의 정보를 모음
        temp_edges = []
        for i in range(len(one_way)):
            x = one_way[i]
            obj_i = infor[x][0]
            value = a[x]
            a[x] = 0
            a[obj_i] += value
            k += abs(value)
            infor[x] = [-1]
            temp_edges += [[obj_i, x]]
        # 단일 간선 노드들의 관계를 끊음
        for i in range(len(temp_edges)):
            print(temp_edges[i][0])
            print(temp_edges[i][1])
            infor[temp_edges[i][0]].remove(temp_edges[i][1])


        cnt = 0
        for i in range(N):
            if a[i] != 0:
                cnt += 1
        if cnt == 0 or cnt == 1:
            break

    if cnt == 0:
        answer = k
    else :
        answer = -1
    return answer


print(solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]]))