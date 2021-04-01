import sys
sys.stdin = open("3752_input.txt")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    scores = list(map(int,input().split()))
    point = [1] + [0] * (sum(scores)+1)

    res = [0]
    for i in range(N):                # N
        for j in range(len(res)):     # 2^(N-1)
            if not point[scores[i]+res[j]]:
                point[scores[i] + res[j]] = 1

                res.append(scores[i] + res[j])

    print('#{} {}'.format(tc, len(res)))