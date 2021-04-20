import sys
sys.stdin = open("1486_input.txt")

T = int(input())

for tc in range(1,T+1):
    N,B = map(int, input().split())
    arr = list(map(int, input().split()))
    sum_v = sum(arr)
    min_v = 10000*N
    for i in range(2**N):
        tall = 0
        for j in range(N):
            if i & (1<<j):
                tall += arr[j]
        if min_v > tall >= B:
            min_v = tall
    res = min_v
    print('#{} {}'.format(tc,res-B))

