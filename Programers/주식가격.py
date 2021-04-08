def solution(prices):
    N = len(prices)

    answer = [0]*N
    stack = []
    # stack[] = [index, value]
    for i in range(N):
        if stack and stack[-1][1] > prices[i]:
            while stack and stack[-1][1] > prices[i]:
                temp = stack.pop(-1)
                answer[temp[0]] = i - temp[0]
        stack += [[i, prices[i]]]
    else:
        while stack:
            temp = stack.pop(-1)
            answer[temp[0]] = i - temp[0]



    return answer

print(solution([1, 2, 3, 2, 3]))