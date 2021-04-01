import sys
sys.stdin = open("3499_input.txt")

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    lst = list(input().split())
    res = []
    if N % 2 :
        for i in range(N // 2):
            res += [lst[i]]
            res += [lst[N // 2 + i+1]]
        res += [lst[N//2]]

    else:
        for i in range(N // 2):
            res += [lst[i]]
            res += [lst[N // 2 + i]]

    print('#{} '.format(tc),end='')
    print(*res)
