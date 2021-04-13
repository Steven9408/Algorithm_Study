import sys
sys.stdin = open("5186_input.txt")

T = int(input())
def demi_to_binary(demi):
    res = ''
    for n in range(-1,-14,-1):
        if demi >= 2**n:
            demi -= 2**n
            res += '1'
        else:
            res += '0'
        if not demi:
            return res
    return 'overflow'

for tc in range(1, T+1):

    N = float(input())
    print('#{} {}'.format(tc, demi_to_binary(N)))