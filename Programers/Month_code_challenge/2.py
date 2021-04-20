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

    while True:
        M = len(edges)
        many = [0] * N

        # 연결된 간선을 파악
        for i in range(M):
            many[edges[i][0]] += 1
            many[edges[i][1]] += 1

        # 간선이 하나인 노드의 인덱스 추출
        one_way = []
        for i in range(N):
            if many[i] == 1:
                one_way += [i]
        # 간선이 하나인 노드를 부모에게 더해주고, 해당간선의 정보를 모음
        temp_edges = []
        for i in range(len(one_way)):
            x = one_way[i]
            for j in range(M):
                if edges[j][0] == x:
                    a[edges[j][1]] += a[x]
                    k += abs(a[x])
                    a[x] = 0
                    edges[j] = [-1, -1]
                    break
                elif edges[j][1] == x:
                    a[edges[j][0]] += a[x]
                    k += abs(a[x])
                    a[x] = 0
                    edges[j] = [-1,-1]
                    break
        # 단일 간선 노드들의 관계를 끊음

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