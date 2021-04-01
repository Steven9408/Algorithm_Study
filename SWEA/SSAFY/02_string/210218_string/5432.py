import sys
sys.stdin = open("5432_input.txt")

def razar(str1):
    N = len(str1)
    res = 1
    if not str1:
        return 0
    else:
        left_index = 0
        right_index = 1
        cnt_l = 1
        for i in range(left_index+1, N):
            if str1[i] == '(':
                cnt_l += 1
            elif str1[i] == ')':
                cnt_l -= 1
            if cnt_l == 0:
                right_index = i
                break
        if left_index + 1 == right_index:
            res = 0
        else:
            for i in range(left_index+1,right_index):
                if str1[i] == '(' and str1[i+1] == ')':
                    res += 1
    str2 = ''
    str3 = ''
    for i in range(left_index+1,right_index):
        str2 += str1[i]
    for i in range(right_index+1,N):
        str3 += str1[i]

    return res + razar(str2) + razar(str3)

T = int(input())
for tc in range(1, T+1):
    str1 = str(input())
    res = razar(str1)
    print('#{} {}'.format(tc, res))