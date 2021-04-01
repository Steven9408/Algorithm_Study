def solution(board, moves):
    N = len(board)
    M = len(moves)
    stack = []
    answer = 0
    for t in range(M):
        for i in range(N):
            temp = board[i][moves[t]-1]
            if temp != 0:
                board[i][moves[t]-1] = 0
                stack += [temp]
                break
        if len(stack) > 1 and (stack[-1] == stack[-2]):
            stack.pop(-1)
            stack.pop(-1)
            answer += 2
    return answer