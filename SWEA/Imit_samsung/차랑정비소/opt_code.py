import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1,T+1):
    N,M,K,A,B = list(map(int,input().split()))

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    tk = list(map(int, input().split()))

    # check_  = [고객번호,들어온시간]
    check_N = [[-1,-1]] * N
    check_M = [[-1,-1]] * M
    use_A = []
    use_B = []
    queue_N = []
    queue_M = []
    t = 0
    k = 0
    end_k = 0

    while end_k < K:
        # 정비가 완료된 인원을 뺀다.
        for i in range(M):
            if check_M[i][0] != -1 and b[i] == t - check_M[i][1]:
                check_M[i] = [-1, -1]

        # 접수가 완료된 인원을 뺀다. 그리고 queue_M에 넣는다
        temp = []
        for i in range(N):
            if check_N[i][0] != -1 and a[i] == t - check_N[i][1]:
                if i == A-1:
                    use_A += [check_N[i][0]]
                temp += [check_N[i][0]]
                check_N[i] = [-1, -1]
        if temp:
            queue_M += temp

        # 정비 대기열을 정비 창구에 넣는다.
        for i in range(M):
            if check_M[i][0] == -1:
                if queue_M:
                    check_M[i] = [queue_M.pop(0), t]
                    if i == B - 1:
                        use_B += [check_M[i][0]]
                    end_k += 1


        # 도착 인원을 접수 대기열에 넣는다.
        while k < K and tk[k] <= t:
            queue_N += [k]
            k += 1

        # 접수 대기열을 접수 창구에 넣는다.
        for i in range(N):
            if check_N[i][0] == -1:
                if queue_N:
                    check_N[i] = [queue_N.pop(0), t]

        t += 1

    res = 0
    for i in range(len(use_A)):
        for j in range(len(use_B)):
            if use_A[i] == use_B[j]:
                res += use_A[i]+1
                break
    if res == 0:
        res = -1
    print('#{} {}'.format(tc,res))
