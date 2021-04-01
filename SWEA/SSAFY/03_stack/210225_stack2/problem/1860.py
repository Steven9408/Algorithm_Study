import sys
sys.stdin = open('1860_input.txt')

T = int(input())

for tc in range(1, T+1):

    N, M, K = map(int, input().split())
    visitor = list(map(int, input().split()))
    res = 'Possible'
    old_time = 0
    sell = 0

    for i in range(N):
        min_v = visitor[i]
        min_idex = i
        for j in range(i,N):
            if min_v > visitor[j]:
                min_v = visitor[j]
                min_idex = j
        visitor[i], visitor[min_idex] = visitor[min_idex], visitor[i]

    for i in range(N):
        now_time = visitor[i]
        product = now_time//M*K
        sell += 1
        if product - sell < 0:
            res = 'Impossible'
            break
        old_time = now_time
    print('#{} {}'.format(tc,res))
