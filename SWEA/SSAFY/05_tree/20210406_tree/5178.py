import sys
sys.stdin = open("5178_input.txt")

T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0]*(N+1)

    for i in range(M):
        n, v = map(int, input().split())
        tree[n] = v
    for i in range(N,0,-1):
        if tree[i] == 0:
            if 2*i+1 <= N:
                tree[i] = tree[2*i] + tree[2*i+1]
            else:
                tree[i] = tree[2 * i]
    print('#{} {}'.format(tc, tree[L]))
