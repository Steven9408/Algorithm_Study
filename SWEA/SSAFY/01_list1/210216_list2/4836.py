import sys
sys.stdin = open("4836_input.txt")

T = int(input())

for tc in range(1,T+1):
    reds = []
    blues = []
    res = 0
    N = 10
    for i in range(int(input())):
        data = list(map(int, input().split()))
        if data[4] == 1 :
            reds += [data]
        else:
            blues += [data]
    area = [[0]*10 for _ in range(10)]
    for red in range(len(reds)):
        for i in range(N):
            for j in range(N):
                if reds[red][1] <= i <= reds[red][3] and reds[red][0] <= j <= reds[red][2]:
                    area[i][j] = 1
    for blue in range(len(blues)):
        for i in range(N):
            for j in range(N):
                if blues[blue][1] <= i <= blues[blue][3] and blues[blue][0] <= j <= blues[blue][2] and area[i][j] == 1:
                    res += 1

    print('#{} {}'.format(tc, res))



