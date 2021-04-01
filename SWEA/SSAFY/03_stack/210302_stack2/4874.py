import sys
sys.stdin = open("4874_input.txt")

T = int(input())

for tc in range(1, T+1):
    lst = list(input().split())
    N = len(lst)
    res = 0
    stack = []

    print('#{}'.format(tc), end=' ')



    for i in range(N):
        if lst[i] == '.':
            if len(stack) == 1:
                print(stack.pop())

        elif lst[i] == '+' or lst[i] == '-' or lst[i] == '*' or lst[i] == '/':
            if len(stack) < 2:
                print('error')
                stack = []
                break
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            if lst[i] == '+':
                stack.append(num1 + num2)
            elif lst[i] == '-':
                stack.append(num1 - num2)
            elif lst[i] == '*':
                stack.append(num1 * num2)
            elif lst[i] == '/':
                stack.append(num1 // num2)
        else:
            stack.append(lst[i])
        print(stack)
    if stack:
        print('error')

