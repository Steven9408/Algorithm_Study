import sys
sys.stdin = open("4861_input.txt")

T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    arry = []
    res = ''
    for i in range(N):
        arry += [str(input())]
    for i in range(N):
        for j in range(N-M+1):
            for k in range(M//2):
                if arry[i][j+k] != arry[i][j+M-1-k]:
                    break
            else:
                for m in range(j,j+M):
                    res += str(arry[i][m])
                break
    if not res:
        for j in range(N):
            for i in range(N - M + 1):
                for k in range(M // 2):
                    if arry[i + k][j] != arry[i + M - 1 - k][j]:
                        break
                else:
                    for m in range(i, i + M):
                        res += str(arry[m][j])
                    break



    print('#{} {}'.format(tc, res))

