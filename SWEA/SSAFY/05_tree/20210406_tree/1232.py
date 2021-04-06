import sys
sys.stdin = open("1232_input.txt")

T = 10

for tc in range(1, T+1):
    N = int(input())
    arr= [[0]]
    tree = [None]*(N+1)
    for i in range(1,N+1):
        arr += [list(input().split())]
        if len(arr[i]) == 2:
            tree[int(arr[i][0])] = int(arr[i][1])

    for i in range(N,0,-1):
        if len(arr[i]) != 2:
            a0, a1, a2, a3 = int(arr[i][0]), arr[i][1], int(arr[i][2]), int(arr[i][3])
            if a1 == '+':
                tree[a0] = tree[a2] + tree[a3]
            elif a1 == '-':
                tree[a0] = tree[a2] - tree[a3]
            elif a1 == '*':
                tree[a0] = tree[a2] * tree[a3]
            else:
                tree[a0] = tree[a2] / tree[a3]
    print('#{} {}'.format(tc, int(tree[1])))