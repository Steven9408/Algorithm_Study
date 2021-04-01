import sys
sys.stdin = open("4881_input.txt")

T = int(input())


def pert(idx,sum_v):
    global res
    if idx == N:
        if sum_v < res:
            res = sum_v

    else:
        for i in range(N):
            if not check[i]:
                per_arr[idx] = order[i]
                check[i] = 1
                sum_v += plane[idx][per_arr[idx]]

                if sum_v > res:
                    check[i] = 0
                    sum_v -= plane[idx][per_arr[idx]]
                    continue
                pert(idx + 1,sum_v)
                check[i] = 0
                sum_v -= plane[idx][per_arr[idx]]

for tc in range(1, T+1):
    N = int(input())
    plane = []

    for i in range(N):
        plane += [list(map(int, input().split()))]

    order = list(range(N))
    check = [0]*N
    per_arr = [0]*N
    res = 50*N


    pert(0,0)
    print('#{} {}'.format(tc,res))