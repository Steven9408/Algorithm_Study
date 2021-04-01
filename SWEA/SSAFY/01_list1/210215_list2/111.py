def absol(a):
    if a > 0:
        return a
    else:
        return -1*a


arr = [[1,2,3,4,5],
       [1,2,3,4,5],
       [1,2,3,4,5],
       [1,2,3,4,5],
       [1,2,3,4,5]]
N = 5
M = 5

dr = [-1,0,1,0]
dc = [0,1,0,-1]
res = 0
for i in range(N):
    for j in range(M):
        sum  =  0
        for k in range(4):
            n_r = i + dr[k]
            n_c = j + dc[k]
            if (0 <= n_r < N) and (0 <= n_c < M):
                sum += absol(arr[i][j]-arr[n_r][n_c])
        print(sum,end=" ")
    print()