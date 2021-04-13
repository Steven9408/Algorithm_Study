import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    dc = 1

    res = []
    for i_1 in range(N):
        for j_1 in range(N):
            for i_2 in range(N):
                for j_2 in range(N):
                    for k1 in range(M):
                        plane = [[0] * N for _ in range(N)]
                        temp = []
                        if j_1+dc*k1 < N:
                            plane[i_1][j_1+dc*k1] = 1
                            temp += [arr[i_1][j_1+dc*k1]]
                        else:
                            break
                        for k2 in range(M):
                            if (j_2+dc*k2 < N) and (not plane[i_2][j_2+dc*k2]):
                                temp += [arr[i_2][j_2+dc*k1]]
                            else:
                                break
                        if sum(temp) <= C:
                            res += [temp]
    print(res)








