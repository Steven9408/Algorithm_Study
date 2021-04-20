def solution(s):
    s = list(s)
    N = len(s)
    answer = 0
    if N == 1:
        return 0
    sol = sol = {')':'(', '}':'{', ']':'['}

    for i in range(N):
        temp = list(s)
        stack = [temp.pop(0)]
        wrong = False
        while temp:
            a = temp.pop(0)
            if a == '(' or a == '{' or a == '[':
                stack += [a]
            else:
                if stack and stack[-1] == sol[a]:
                    stack.pop(-1)
                else:
                    wrong = True
                    break
            if stack and not temp:
                wrong = True
                break
        if not wrong:
            answer += 1
        s += s.pop(0)


    return answer
print(solution("["))
