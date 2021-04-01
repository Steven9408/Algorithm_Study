import sys
sys.stdin = open("4864_input.txt")

T = int(input())

for tc in range(1,T+1):
    str1 = str(input())
    str2 = str(input())

    N = len(str1)
    M = len(str2)
    i = 0
    j = 0

    while i < N and j < M:
        if str1[i] != str2[j]:
            j = j - i
            i = -1
        j += 1
        i += 1
    if i == N:
        res = 1
    else:
        res = 0

    print('#{} {}'.format(tc,res))
