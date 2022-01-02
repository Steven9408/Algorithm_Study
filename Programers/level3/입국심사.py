# def solution(n, times):
#     M = len(times)
#     max_t = (n//M+1) * max(times)
#     check = [1]*M
#     cnt = 0
#
#     for t in range(1,max_t):
#         if cnt >= n:
#             break
#         for i in range(M):
#             if check[i] == times[i]:
#                 cnt += 1
#                 check[i] = 0
#             check[i] += 1
#     answer = t-1
#     return answer

def solution(n, times):
    M = len(times)
    max_t = (n//M+1) * max(times)
    l = 0
    r = max_t
    while l <= r:
        m = (l+r)//2
        cnt = 0
        for i in range(M):
            cnt += m//times[i]
            if cnt >= n:
                break
        if cnt >= n:
            r = m-1
        else:
            l = m+1


    return m




print(solution(6,[7, 10]))