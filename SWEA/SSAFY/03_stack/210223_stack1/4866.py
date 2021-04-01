import sys
sys.stdin = open("4866_input.txt")

T = int(input())

for tc in range(1,T+1):
    str1 = input()
    stack = []
    res = 1

    for i in range(len(str1)):
        if str1[i] == '{' or str1[i] == '(':
            stack.append(str1[i])
        elif str1[i] == '}' or str1[i] == ')':
            if not stack:
                res = 0
                break
            temp = stack.pop()
            if str1[i] == '}':
                if temp != '{':
                    res = 0
                    break
            if str1[i] == ')':
                if temp != '(':
                    res = 0
                    break
    if stack:
        res = 0
    print('#{} {}'.format(tc,res))
