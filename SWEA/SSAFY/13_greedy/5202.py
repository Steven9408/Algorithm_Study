import sys
sys.stdin = open("5202_input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))

    arr.sort(key=lambda x: x[-1])
    res = 1
    select = arr.pop(0)
    while arr:
        now = arr.pop(0)
        if select[1] <= now[0]:
            select = list(now)
            res += 1
    print('#{} {}'.format(tc,res))

