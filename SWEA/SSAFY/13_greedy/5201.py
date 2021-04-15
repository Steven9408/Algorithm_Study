import sys
sys.stdin = open("5201_input.txt")

T = int(input())

def sol(k):
    global container_check
    global max_v

    if k == N:
        sum_v = 0
        for i in range(N):
            if container_check[i]:
                sum_v += container[i]
        if max_v < sum_v:
            max_v = sum_v


    else:
        weight = container[k]
        for i in range(M):
            if truck[i] >= weight:
                truck[i] -= weight
                container_check[k] = 1
                sol(k+1)
                truck[i] += weight
                container_check[k] = 0
        sol(k+1)

for tc in range(1, T+1):
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    max_v = 0
    container_check = [0]*N

    sol(0)

    print('#{} {}'.format(tc, max_v))

