import sys
sys.stdin = open("4613_input.txt")

T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = []
    res = []

    for i in range(N):
        arr += [' '.join(input()).split()]

    for i in range(1,N-1):
        for j in range(1,N-i):
            k = N - i - j
            cnt = 0
            for a in range(N):
                if 0 <= a < i:
                    obj = 'W'
                elif i <= a < j+i:
                    obj = 'B'
                else:
                    obj = 'R'
                for b in range(M):
                    if arr[a][b] != obj:
                        cnt += 1
            res += [cnt]

    min_v = res[0]
    for i in range(len(res)):
        if min_v > res[i]:
            min_v = res[i]
    print('#{} {}'.format(tc,min_v))