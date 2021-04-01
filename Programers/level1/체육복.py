def solution(n, lost, reserve):
    stu = [1] * n

    for i in range(len(reserve)):
        stu[reserve[i]-1] += 1

    for i in range(len(lost)):
        stu[lost[i] - 1] -= 1

    reserve = list(set(reserve) - set(lost))

    answer = 0
    N = len(reserve)
    M = 2 ** N

    for i in range(M):
        temp = list(stu)
        for j in range(N):
            if i & (1 << j):
                if reserve[j] - 1 != n - 1:
                    temp[reserve[j]] += 1
            else:
                if reserve[j] - 1 != 0:
                    temp[reserve[j] - 2] += 1
        cnt = 0
        for j in range(n):
            if temp[j]:
                cnt += 1
        if cnt > answer:
            answer = cnt
    return answer