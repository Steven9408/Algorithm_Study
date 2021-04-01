import sys
sys.stdin = open("1216_input.txt")

def palindrome(M,N):
    global arry
    for i in range(N):
        for j in range(N - M + 1):
            for k in range(M // 2):
                if arry[i][j + k] != arry[i][j + M - 1 - k]:
                    break
            else:
                return M

    for j in range(N):
        for i in range(N - M + 1): #
            for k in range(M // 2):
                if arry[i + k][j] != arry[i + M - 1 - k][j]:
                    break
            else:
                return M
    return 1

T = 10
for tc in range(1,T+1):
    text_number = int(input())
    arry = []
    N = 100
    for i in range(N):
        arry += [str(input())]
    for i in range(N,1,-1):
        res = palindrome(i,N)
        if res != 1:
            break


    print('#{} {}'.format(tc, res))

