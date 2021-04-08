
def solution(nums):
    def con(idex, cnt):
        global res
        if idex >= N:
            if cnt == N // 2:
                lst = []
                for i in range(N):
                    if select[i] == 1:
                        lst += [nums[i]]
                temp = len(set(lst))
                if temp > res:
                    res = temp
        else:
            if cnt < (N // 2):
                select[idex] = 1
                cnt += 1
                con(idex + 1, cnt)
                cnt -= 1
                select[idex] = 0
            con(idex + 1, cnt)


    N = len(nums)
    select = [0]*N
    cnt = 0
    global res
    res = 0



    con(0,cnt)
    answer = res
    return answer




solution([3,1,2,3])