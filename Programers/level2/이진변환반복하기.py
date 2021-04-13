def demi_to_bin(str1):
    N = 0
    cnt = 0
    res = ''
    for i in str1:
        if i != '0':
            N += 1
        else:
            cnt += 1
    while N != 0:
        res = str(N % 2) + res
        N //= 2
    return (res, cnt)


def solution(s):
    cnt_res = 0
    k = 0
    while s != '1':
        s, cnt = demi_to_bin(s)
        cnt_res += cnt
        k += 1
    answer = [k, cnt_res]
    return answer