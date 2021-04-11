import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    res = 0
    N_house = 0
    for i in range(N):
        data = list(map(int, input().split()))
        arr += [data]
        for j in range(N):
            if data[j]:
               N_house += 1

    # max_k 결정
    max_k = -1
    for i in range(N+2):
        if N_house*M >= i*i+(i-1)*(i-1):
            max_k = i

    for k in range(1,max_k+1):
        cost = k*k+(k-1)*(k-1)
        for i in range(N):
            for j in range(N):
                cnt = 0
                for i_s in range(-k+1,1):
                    for j_s in range(-i_s-k+1,(k+i_s-1)*2+1-i_s-k+1):
                        i_abs = i_s + i
                        j_abs = j_s + j
                        if (0 <= i_abs < N) and (0 <= j_abs < N) and arr[i_abs][j_abs] == 1:
                            cnt += 1

                for i_s in range(1,k):
                    for j_s in range(-k+i_s+1,k+k-1-2*i_s-k+i_s+1):
                        i_abs = i_s + i
                        j_abs = j_s + j
                        if (0 <= i_abs < N) and (0 <= j_abs < N) and arr[i_abs][j_abs] == 1:
                            cnt += 1
                if cnt*M >= cost and res < cnt:
                    res = cnt

    print('#{} {}'.format(tc,res))









