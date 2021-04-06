import sys
sys.stdin = open("input.txt")

T = 10

for tc in range(1, T+1):
    N = int(input())
    arr = [[0]]
    res = ''
    for i in range(N):
        arr += [input().split()]

    def inorder(v):
        global res
        M = len(arr[v])
        if M < 3:
            res += arr[v][1]
        else:
            inorder(int(arr[v][2]))
            res += arr[v][1]
            if M != 3:
                inorder(int(arr[v][3]))
        return

    inorder(1)
    print('#{} {}'.format(tc,res))


