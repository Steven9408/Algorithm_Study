import sys
sys.stdin  = open("1974_input.txt")

def serch_wrong(arry):
    M = 9
    for i in range(M):
        for j in range(i+1,M):
            if arry[i] == arry[j]:
                return 0
    return 1

T = int(input())

for test_case in range(1,T+1):
    arry = []
    N = 9
    res = 1
    for i in range(N):
        arry.append(list(map(int, input().split())))
        res *= serch_wrong(arry[i])

    for j in range(N):
        temp = []
        for i in range(N):
            temp += [arry[i][j]]
        res *= serch_wrong(temp)

    for i in range(N//3):
        for j in range(N//3):
            temp = []
            for i_s in range(3):
                for j_s in range(3):
                    temp += [arry[i*3+i_s][j*3+j_s]]
            res *= serch_wrong(temp)

    print(f'#{test_case} {res}')
