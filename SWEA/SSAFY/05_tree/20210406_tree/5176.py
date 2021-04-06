import sys
sys.stdin = open("5176_input.txt")

T = int(input())

def inorder(n):
    global cnt
    if  n >= len(lst) or lst[n] != -1:
        return
    else:
        inorder(2*n)
        lst[n] = cnt
        cnt += 1
        inorder(2*n+1)


for tc in range(1, T+1):
    N = int(input())
    k=1
    lst = [0] + [-1]*N
    cnt = 1
    inorder(1)
    res1 = lst[1]
    res2 = lst[N//2]

    print('#{} {} {}'.format(tc, res1, res2))

