def solution(n):
    res = [[0] * n for _ in range(n)]
    answer = []
    i_r, j_r = -1, 0
    k = 1
    for i in range(n):
        for j in range(i, n):

            if i % 3 == 0:
                i_r += 1

            elif i % 3 == 1:
                j_r += 1

            elif i % 3 == 2:
                i_r -= 1
                j_r -= 1

            res[i_r][j_r] = k
            k += 1

    for i in res:
        for j in i:
            if j != 0:
                answer.append(j)
    return answer