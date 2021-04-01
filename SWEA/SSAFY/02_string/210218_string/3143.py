import sys
sys.stdin = open("3143_input.txt")

T = int(input())
for tc in range(1,T+1):
    str1,str2 = input().split()
    N1 = len(str1)
    N2 = len(str2)
    cnt = 0
    for i in range(N1-N2+1):
        if str1[i:i+N2] == str2:
            print(str1[i:i+N2], str2)
            cnt += 1
    res = N1 - cnt*(N2-1)
    print('#{} {}'.format(tc, res))