
def solution(triangle):
    N = len(triangle)

    for i in range(1,N):
        triangle[i][0] += triangle[i-1][0]
        triangle[i][i] += triangle[i-1][i-1]
        for j in range(1,i):
            temp1 = triangle[i-1][j-1] + triangle[i][j]
            temp2 = triangle[i-1][j] + triangle[i][j]
            triangle[i][j] = max([temp1,temp2])


    answer = max(triangle[N-1])
    return answer



solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])