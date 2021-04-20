import sys
sys.stdin = open("1865_input.txt")

T = int(input())

def dfs(idx,pro):
    global max_p
    if idx == N:
        if max_p < pro:
            max_p = pro
        return
    else:
        for i in range(N-1,-1,-1):
            if not check[i]:
                new_pro = pro * (arr[idx][i])
                if new_pro > max_p:
                    check[i] = 1
                    dfs(idx+1, new_pro)
                    check[i] = 0


for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr[i][j] /= float(100)
    check = [0] * N
    max_p = 0
    dfs(0,1)
    print('#{} {:.6f}'.format(tc,round(max_p*100,6)))
