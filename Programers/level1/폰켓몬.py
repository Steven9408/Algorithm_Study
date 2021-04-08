def solution(nums):
    N = len(nums)
    cnt = len(set(nums))

    if cnt >= N//2:
        answer = N//2
    else:
        answer = cnt


    return answer
print(solution([3,3,3,2,2,2]))
