import sys
sys.stdin = open("4865_input.txt")

T = int(input())

for tc in range(1, T+1):
    str1 = str(input())
    str2 = str(input())

    max_cnt = 0

    for i in range(len(str1)):
        cnt = 0
        for j in range(len(str2)):
            if str2[j] == str1[i]:
                cnt += 1
        if max_cnt < cnt:
            max_cnt = cnt

    print('#{} {}'.format(tc, max_cnt))

