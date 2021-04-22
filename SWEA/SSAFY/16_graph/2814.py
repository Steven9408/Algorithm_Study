import sys
sys.stdin = open("2814_input.txt")

T = int(input())


for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*N for _ in range(N)]
    for i in range(M):
        s,e = map(int, input().split())
        arr[s-1][e-1] = 1
    visitied = [0]*N

    max_route = []
    queue = []
    for i in range(N):
        temp_depth = []
        if not visitied[i]:
            visitied[i] = 1
            queue.append([i,1])
            while queue:
                now = queue.pop(0)
                for j in range(N):
                    if arr[now[0]][j]:
                        visitied[j] = 1
                        queue.append([j,now[1]+1])
                else:
                    temp_depth.append(now[1]+1)
        temp = sorted(temp_depth,reverse=True)
        if len(temp) == 1:
            max_route.append(temp[0])
        else:
            max_route.append(temp[0]+temp[1]-1)
    print(max_route)






