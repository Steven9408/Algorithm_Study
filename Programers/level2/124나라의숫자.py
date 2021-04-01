def solution(n):
    number = [1,2,4]
    answer = ''
    while n:
        answer = str(number[(n-1)%3]) + answer
        n=(n-1)//3
    return answer