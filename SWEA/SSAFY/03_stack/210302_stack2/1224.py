import sys
sys.stdin = open("1224_input.txt")

T = 10

for tc in range(1, T + 1):
    N = int(input())
    stack = []
    isp = {'*': 2, '+': 1, '(': 0}
    icp = {'*': 2, '+': 1, '(': 3}

    str1 = input()
    new = []

    for i in range(N):
        token = str1[i]
        if token == '*' or token == '+' or token == '(':
            if not stack or isp[stack[-1]] < icp[token]:
                stack.append(token)
            else:
                while stack and icp[token] <= isp[stack[-1]]:
                    new += [stack.pop()]
                stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                new += [stack.pop()]
            stack.pop()
        else:
            new += [token]
    else:
        c = len(stack)
        for j in range(c):
            new += [stack.pop()]

    for i in range(len(new)):
        if new[i] == '*':
            stack.append(int(stack.pop()) * int(stack.pop()))
        elif new[i] == '+':
            stack.append(int(stack.pop()) + int(stack.pop()))
        else:
            stack.append(new[i])
    print('#{} {}'.format(tc, stack[-1]))