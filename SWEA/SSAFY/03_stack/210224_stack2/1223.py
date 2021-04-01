import sys
sys.stdin = open("1223_input.txt")

T = 10

for tc in range(1,T+1):
    N = int(input())
    stack = []
    pri = {'*' : 2 ,'+' : 1}

    str1 = input()
    new = []

    for i in range(N):
        token = str1[i]
        if token == '*' or token == '+':
            if not stack or pri[stack[-1]] < pri[token]:
                stack.append(token)
            else:
                while stack and pri[token] <= pri[stack[-1]]:
                    new += [stack.pop()]
                stack.append(token)
        else:
            new += [token]
    else:
        c=len(stack)
        for j in range(c):
            new += [stack.pop()]

    for i in range(len(new)):
        if new[i] == '*':
            stack.append(int(stack.pop()) * int(stack.pop()))
        elif new[i] == '+':
            stack.append(int(stack.pop()) + int(stack.pop()))
        else:
            stack.append(new[i])
    print('#{} {}'.format(tc,stack[-1]))



