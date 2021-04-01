def solution(numbers):
    N = len(numbers)
    numbers.sort()
    answer = []
    for i in range(N):
        for j in range(i+1,N):
            answer += [numbers[i]+numbers[j]]
    answer = list(set(answer))
    answer.sort()
    return answer