import sys
sys.stdin = open("1219_input.txt")

T = 10

for tc in range(1,T+1):
    trash, E = list(map(int,input().split()))
    N = 100
    route = [[-1]*N for _ in range(2)]
    temp = list(map(int,input().split()))
    for i in range(0,len(temp),2):
        if route[0][temp[i]] == -1:
            route[0][temp[i]] = temp[i+1]
        else:
            route[1][temp[i]] = temp[i+1]
    res = 0

    stack = [0]
    visitied = [0]*N
    visitied[0] = 1

    while stack1:
        top = stack.pop()
        if top == 99:
            res = 1
            break
        for i in range(2):
            if visitied[route[i][top]] == 0 and route[i][top] != -1:
                stack.append(route[i][top])
                visitied[route[i][top]] = 1
    print('#{} {}'.format(tc,res))






