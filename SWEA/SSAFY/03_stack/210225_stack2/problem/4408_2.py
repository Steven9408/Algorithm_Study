import sys
sys.stdin = open('4408_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    students = []
    res = 0
    route = [0]*200
    for i in range(N):
        students += [list(map(int, input().split()))]
        max_j = (students[i][1] - 1) // 2
        min_j = (students[i][0] - 1) // 2
        if max_j >= min_j:
            for j in range(min_j, max_j + 1):
                route[j] += 1
        else:
            for j in range(max_j, min_j + 1):
                route[j] += 1

    for i in range(len(route)):
        if res < route[i]:
            res = route[i]
    print('#{} {}'.format(tc, res))
