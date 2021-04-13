import sys
sys.stdin = open("5158_input.txt")

T = int(input())
# 0100 0111 1111 1110
def hetax_to_binary(chr):
    res = ''
    if ord('0') <= ord(chr) <= ord('9'):
        demi = ord(chr) - ord('0')
    else:
        demi = 10 + ord(chr) - ord('A')
    for n in range(0,4):
        res = str(demi%2) + res
        demi //= 2
    return res

for tc in range(1, T+1):
    N, hexa = input().split()
    N = int(N)

    res = ''

    for chr in hexa:
        res += hetax_to_binary(chr)

    print('#{} {}'.format(tc, res))




