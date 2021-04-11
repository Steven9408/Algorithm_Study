import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    house_list = []
    res = 0
    N_house = 0
    for i in range(N):
        data = list(map(int, input().split()))
        arr += [data]
        for j in range(N):
            if data[j]:
                N_house += 1
                house_list += [[i,j]]

    # max_k 결정
    max_k = -1
    for i in range(N+2):
        if N_house*M >= i*i+(i-1)*(i-1):
            max_k = i

    for k in range(max_k,0,-1):
        cost = k*k+(k-1)*(k-1)
        for i in range(N):
            for j in range(N):
                cnt = 0
                for c in range(N_house):
                    dis = abs(i-house_list[c][0]) + abs(j-house_list[c][1])
                    if dis < k:
                        cnt += 1
                if cnt*M >= cost and res < cnt:
                    res = cnt
        if res:
            break

    print('#{} {}'.format(tc,res))

