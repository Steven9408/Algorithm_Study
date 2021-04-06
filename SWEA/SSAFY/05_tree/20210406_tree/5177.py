import sys
sys.stdin = open("5177_input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = [-1]+list(map(int, input().split()))
    tree = [-1]*(N+1)

    tree[1] = lst[1]
    for i in range(2,N+1):
        tree[i] = lst[i]
        while i !=1:
            if tree[i//2] > tree[i]:
                tree[i // 2], tree[i] = tree[i], tree[i // 2]
                i = i//2
            else:
                break
    res = 0
    i = N//2
    while i:
        res += tree[i]
        i = i//2
    print('#{} {}'.format(tc, res))
