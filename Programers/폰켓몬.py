def solution(nums):
    N = len(nums)
    arr = [0]*(max(nums)+1)
    M=len(arr)
    cnt = 0
    cnt = len(set(nums))
    # for i in range(max(nums)+1):
    #     for j in range(N):
    #         if i == nums[j]:
    #             arr[i] += 1
    #             cnt += 1
    #             break
    if cnt >= N//2:
        answer = N//2
    else:
        answer = cnt


    return answer
print(solution([3,3,3,2,2,2]))
