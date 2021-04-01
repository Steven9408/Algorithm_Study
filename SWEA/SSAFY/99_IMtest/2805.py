import sys
sys.stdin = open("2805_input.txt")

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = []
    for i in range(N):
        arr += [list(map(int, ' '.join(input()).split()))]
    res = 0
    for i in range(N):
        min_j = N//2-i
        max_j = N//2+i
        if i > N//2:
            min_j = (i-N//2)
            max_j = N-(i-N//2+1)
        for j in range(min_j,max_j+1):
            res += arr[i][j]

    print('#{} {}'.format(tc,res))


