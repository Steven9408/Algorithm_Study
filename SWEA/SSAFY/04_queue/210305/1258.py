import sys
sys.stdin = open("1258_input.txt")

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    plane = []

    for i in range(N):
        plane += [list(map(int, input().split()))]

    i_s = 0
    j_s = 0
    infor = []
    res = []
    for i in range(N):
        temp = []
        cnt = 0
        for j in range(N):
            if plane[i][j] and j < N-1:
                if not cnt:
                    start = j
                    cnt = 1
                else:
                    cnt += 1
            else:
                if not cnt:
                    continue
                else:
                    if j == N-1 and plane[i][j]:
                        temp += [[start, start + cnt]]
                    else:
                        temp += [[start,start+cnt-1]]
                    cnt = 0
        infor += [temp]
    for i in range(N):
        for j in range(len(infor[i])):
            if infor[i][j]:
                dy = 1
                dx = infor[i][j][1]-infor[i][j][0]+1
            else:
                continue
            for i_e in range(i+1,N-1):
                yes = 0
                for j_e in range(len(infor[i_e])):
                    if infor[i][j] == infor[i_e][j_e]:
                        yes = 1
                        break
                if yes:
                    dy += 1
                    infor[i_e][j_e] = []
                else:
                    break
            res += [[dy,dx]]

    for i in range(len(res)):
        min_v = res[i][1]*res[i][0]
        min_index = i
        for j in range(i+1,len(res)):
            temp1 = res[j][1]*res[j][0]
            if temp1 < min_v or (temp1 == min_v and res[min_index][0] > res[j][0]):
                min_v = temp1
                min_index = j

        res[i] , res[min_index] = res[min_index], res[i]
    print('#{} {} '.format(tc,len(res)),end='')
    for i in range(len(res)):
        print(*res[i],end=' ')
    print()





