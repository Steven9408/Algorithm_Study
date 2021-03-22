import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1,T+1):
    N,M,K,A,B = list(map(int,input().split()))

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    tk = list(map(int, input().split()))

    # k 고객이 어디를 방문했는지 찾는다(i=0>N:i=1>M)
    check_list = [[0]*K for _ in range(2)]

    # tk를 오름차순으로 정리
    for i in range(K):
        min_v = tk[i]
        min_index = i
        for j in range(i,K):
            if min_v > tk[j]:
                min_v = tk[j]
                min_index = j
        tk[i],tk[min_index] = tk[min_index],tk[i]

    check_N = [[-1,-1]] * N
    check_M = [[-1,-1]] * M
    t = 0
    k = 0
    end_k = 0
    while True:
        for i in range(M):
            if check_M[i][0] !=-1:
                if t-check_M[i][1] == a[i]:
                    if i ==
                    check_M[i][0] = -1



        while tk[k] <= t:


