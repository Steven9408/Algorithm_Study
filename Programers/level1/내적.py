def solution(a, b):
    N = len(a)
    answer = 0
    for i in range(N):
        answer += a[i]*b[i]
    return answer