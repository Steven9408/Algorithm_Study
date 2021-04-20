import sys
sys.stdin = open("4366_input.txt")

def bin_to_deci(a):
    N = len(a)
    res = 0
    for i in range(N):
        res += int(a[N-i-1]) * 2**i
    return res

def tri_to_deci(a):
    N = len(a)
    res = 0
    for i in range(N):
        res += int(a[N - i - 1]) * 3 ** i
    return res





T = int(input())

for i in range(1, T+1):
    bin = input()
    tri = list(map(int,' '.join(input()).split()))
    bin_list = []
    tri_list = []

    for i in range(len(bin)):
        temp = ''
        for j in range(len(bin)):
            if i == j:
                if bin[i] == '1':
                    temp += '0'
                else:
                    temp += '1'
            else:
                temp += bin[j]
        bin_list += [bin_to_deci(temp)]




