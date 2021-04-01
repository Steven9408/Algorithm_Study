import sys
sys.stdin = open("1289_input.txt")

for tc in range(int(input())):
    str1 = list(map(int, (' '.join(input())).split()))
    pure = 0
    cnt = 0
    N = len(str1)

    for i in range(N):
        if str1[i] != pure:
            pure = str1[i]
            cnt += 1
        sum_v = 0
        for j in range(i+1,N):
            sum_v += str1[j]
        if pure*(N-i) == sum_v:
            break
    print('#{} {}'.format(tc+1,cnt))


