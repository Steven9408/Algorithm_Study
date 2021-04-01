import sys
sys.stdin = open("11315_input.txt")

T = int(input())

for tc in range(1,T+1):
    dr = [-1,0,1,0,-1,1,1,-1]
    dc = [0,1,0,-1,1,1,-1,-1]
    N = int(input())
    plane = []
    for i in range(N):
        plane += [' '.join(input()).split()]
    def omok():
        for i in range(N):
            for j in range(N):
                if plane[i][j] == 'o':
                    for k in range(8):
                        cnt = 1
                        r = i
                        c = j
                        while cnt < 5:
                            r = dr[k] + r
                            c = dc[k] + c
                            if 0<=r<N and 0<=c<N and plane[r][c] == 'o':
                                cnt += 1
                            else:
                                break
                        else:
                            return 'YES'

        return 'NO'
    res = omok()
    print('#{} {}'.format(tc,res))