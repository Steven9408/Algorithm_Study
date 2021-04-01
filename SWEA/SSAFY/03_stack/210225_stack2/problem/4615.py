import sys
sys.stdin = open("4615_input.txt")

T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [[0]*N for _ in range(N)]
    dr = [-1, 0, 1, 0, -1, 1, 1, -1]
    dc = [0, 1, 0, -1, 1, 1, -1, -1]

    arr[N // 2 - 1][N // 2 - 1] = 2
    arr[N // 2][N // 2] = 2
    arr[N // 2][N // 2 - 1] = 1
    arr[N // 2 - 1][N // 2] = 1
    for i in range(M):
        data = list(map(int, input().split()))
        arr[data[0]-1][data[1]-1] = data[2]
        for k in range(8):
            r = data[0]-1
            c = data[1]-1
            temp = []
            while True:
                r = r + dr[k]
                c = c + dc[k]
                if c >= N or r >= N or c < 0 or r < 0 or not arr[r][c]:
                    break
                elif arr[r][c] != data[2]:
                    # Keep going
                    temp += [[r, c]]
                elif arr[r][c] == data[2]:
                    # 이전 인덱스들 다 data[2]로 바꿔
                    for j in range(len(temp)):
                        arr[temp[j][0]][temp[j][1]] = data[2]
                    break
    cnt1 = 0
    cnt2 = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                cnt1 += 1
            elif arr[i][j] == 2:
                cnt2 += 1
    print('#{} {} {}'.format(tc, cnt1, cnt2))
