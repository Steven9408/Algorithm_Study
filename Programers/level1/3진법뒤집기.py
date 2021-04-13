def solution(n):
    lst = []
    answer = 0
    while n:
        lst.append(n % 3)
        n = n // 3
    N = len(lst)
    for i in range(N):
        answer += lst[i] * 3 ** (N - i - 1)

    return answer