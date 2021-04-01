T = int(input())
for tc in range(1, T+1):
    str1 = str(input())
    N = len(str1)
    cnt_stick = 0
    res = 0
    i = 0
    while i < N:
        if str1[i] == '(' and str1[i+1] == ')':
            res += cnt_stick
            i += 2
            continue
        elif str1[i] == '(':
            cnt_stick += 1
            i += 1
            continue
        else:
            cnt_stick += -1
            res += 1
            i += 1
            continue
    print('#{} {}'.format(tc, res))



