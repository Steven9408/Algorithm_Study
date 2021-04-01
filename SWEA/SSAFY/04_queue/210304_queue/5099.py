import sys
sys.stdin = open("5099_input.txt")

T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    Q = []
    lst = list(map(int, input().split()))
    check = [0]*M
    Q = [None]*N
    cnt = 0
    k = 0

    while len(Q) > 1:
        now = cnt % N
        if not Q[now]:
            if k < M:
                Q[now] = [k,lst[k]]
                k += 1
            else:
                Q[now] = None
        elif Q[now][1]//2 == 0:
            if k < M:
                check[Q[now][0]] = 1
                Q[now] = [k,lst[k]]
                k += 1
            else:
                check[Q[now][0]] = 1
                Q[now] = None
        else:
            Q[now][1] = Q[now][1]//2
        if sum(check) > M-2:
            break
        cnt += 1

    for i in range(M):
        if check[i] == 0:
            res = i
            break
    print('#{} {}'.format(tc,res+1))