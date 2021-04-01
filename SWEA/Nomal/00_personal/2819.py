import sys
sys.stdin = open('2819_input.txt')

T = int(input())

def moo(idx):
    global lst
    global stack
    if idx == M-1:
        temp = []
        for i in range(len(stack)):
            temp.append(plane[stack[i][0]][stack[i][1]])
        if temp not in lst:
            lst += [temp]
        return
    r, c = stack[-1]
    for i in range(4):
        rn = r + dr[i]
        cn = c + dc[i]
        if 0 <= cn < N and 0 <= rn < N:
            stack.append((rn,cn))
            moo(idx+1)
            stack.pop()


for test_case in range(1,T+1):
    plane = []
    N = 4
    M = 7
    lst = []
    for i in range(N):
        plane.append(list(map(int, input().split())))

    dr = [-1,0,1,0]
    dc = [0,1,0,-1]

    for i in range(N):
        for j in range(N):
            stack = [(i,j)]
            moo(0)

    for i in range(len(lst)):
        print(lst[i])
    print('#{} {}'.format(test_case,len(lst)))




