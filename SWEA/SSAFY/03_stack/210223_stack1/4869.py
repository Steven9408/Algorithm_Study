import sys

sys.stdin = open("4869_input.txt")

T = int(input())
arr = [0] * 31
def problem(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 3
    if not arr[n]:
        arr[n] = problem(n-1)+2*problem(n-2)
    return arr[n]


for tc in range(1,T+1):
    N = int(input())
    res = problem(N//10)
    print('#{} {}'.format(tc,res))








