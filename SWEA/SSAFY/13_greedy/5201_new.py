import sys
sys.stdin = open("5201_input.txt")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    res = 0
    container_check = [0]*N

    for i in range(M):
        temp = 0
        temp_i = -1
        for j in range(N):
            if container_check[j] == 0 and temp <= container[j] and truck[i] >= container[j]:
                temp = container[j]
                temp_i = j
        if temp:
            container_check[temp_i] = 1
            res += temp

    print('#{} {}'.format(tc, res))
