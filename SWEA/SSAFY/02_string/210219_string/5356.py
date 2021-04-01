import sys
sys.stdin = open("5436_input.txt")
T = int(input())
for tc in range(1,T+1):
    arry = []
    N = 5
    res =''

    max_len = 0
    for i in range(N):
        arry += [input()]
        if len(arry[i]) > max_len:
            max_len = len(arry[i])

    for j in range(max_len):
        for i in range(N):
            if len(arry[i]) < j+1:
                continue
            res += arry[i][j]
    print('#{} {}'.format(tc,res))
