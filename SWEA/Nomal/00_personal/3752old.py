T = int(input())
for tc in range(1,T+1):
    N = int(input())
    scores = list(map(int,input().split()))
    res = []
    for i in range(1<<N):  # 2^N
        temp = 0
        for j in range(N): # N
            if i & (1 << j):
                temp += scores[j]
        for j in range(len(res)): # 2^N
            if temp == res[j]:
                break
        else:
            res += [temp]
    print('#{} {}'.format(tc, len(res)))