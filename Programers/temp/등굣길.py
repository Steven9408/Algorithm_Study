def solution(m, n, puddles):
    arr=[[0]*m for _ in range(n)]

    for i in range(len(puddles)):
        arr[puddles[i][1]-1][puddles[i][0]-1] = -1
    arr[n-1][m-1] = 1

    r = min(m,n)
    for i in range(1,r):
        for j in range(n, n-i, -1):
            print(m-i,j)
            arr[m-i-1][j] = 2
    print(arr)
    return 0



print(solution(4,3,[[2,2]]))