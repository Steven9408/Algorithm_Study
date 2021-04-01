import sys
sys.stdin = open('2001_input.txt')

T = int(input())

for test_case in range(1,T+1):
    N, M = map(int, input().split())

    plane= []
    for i in range(N):
        plane += [list(map(int, input().split()))]

    step = N-M+1
    catch = 0
    for i in range(step):
        for j in range(step):
            temp = 0
            for i_s in range(i,i+M):
                for j_s in range(j,j+M):
                    temp += plane[i_s][j_s]
            if catch < temp:
                catch =temp
    print('#{} {}'.format(test_case,catch))