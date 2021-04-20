import sys
sys.stdin = open("1970_input.txt")

moneys = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    M = 8
    cnt = [0]*M
    for i in range(M):
        cnt[i] = N // moneys[i]
        N -= cnt[i] * moneys[i]
    print('#{}'.format(tc))
    print(*cnt)