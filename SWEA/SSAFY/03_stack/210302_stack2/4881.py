import sys
sys.stdin = open("4881_input.txt")

T = int(input())


def pert(idx):
    global res
    if idx == N:
        sum_v = 0
        for k in range(N):
            sum_v += plane[k][per_arr[k]]
        if res > sum_v:
            res = sum_v

    else:
        for i in range(N):
            if not check[i]:
                per_arr[idx] = order[i]
                check[i] = 1
                pert(idx + 1)
                check[i] = 0

for tc in range(1, T+1):
    N = int(input())
    plane = []

    for i in range(N):
        plane += [list(map(int, input().split()))]

    order = list(range(N))
    check = [0]*N
    per_arr = [0]*N
    res = 50*N


    pert(0)
    print('#{} {}'.format(tc,res))