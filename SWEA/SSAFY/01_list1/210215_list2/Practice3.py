N = 5

rect = [[0]*5 for _ in range(5)]
number = 1
dr = [0,1,0,-1]
dc = [1,0,-1,0]

point_r = 0
point_c = 0
k = N
rect[0][0] = number


while number <= N*N:
    for i in range(k-1):
        number += 1
        point_r += dr[0]
        point_c += dc[0]
        rect[point_r][point_c] = number
    for i in range(k-1):
        number += 1
        point_r += dr[1]
        point_c += dc[1]
        rect[point_r][point_c] = number
    for i in range(k-1):
        number += 1
        point_r += dr[2]
        point_c += dc[2]
        rect[point_r][point_c] = number
    for i in range(k-2):
        number += 1
        point_r += dr[3]
        point_c += dc[3]
        rect[point_r][point_c] = number

    number += 1
    point_r += dr[0]
    point_c += dc[0]
    rect[point_r][point_c] = number
    k -= 2

for i in range(N):
    print(rect[i])



