import sys
sys.stdin = open("homework_input.txt")

T = int(input())
number = [
[0,0,0,1,1,0,1],
[0,0,1,1,0,0,1],
[0,0,1,0,0,1,1],
[0,1,1,1,1,0,1],
[0,1,0,0,0,1,1],
[0,1,1,0,0,0,1],
[0,1,0,1,1,1,1],
[0,1,1,1,0,1,1],
[0,1,1,0,1,1,1],
[0,0,0,1,0,1,1]
]


for tc in range(1,T+1):
    N, M = map(int, input().split())
    res = 0
    arr = []
    # 행을 받아서 1이 있는 행을 저장
    for i in range(N):
        arr += [list(map(int, ' '.join(input()).split()))]
        if 1 in arr[i]:
            res = 1
            ob_i = i

    data = list(arr[ob_i])

    # 뒤에서 부터 탐색해서 1이 최초로 발견되는 지점 파악
    for i in range(M-1,-1,-1):
        if data[i] == 1:
            ob_i = i
            break
    else:
        res = 0 # 전체에 1이 없을 때

    for i in range(ob_i-56, -1, -1):
        if data[i] == 1: # 56개의 요소 말고 1이 있을때,
            res = 0
            break
    else:
        res = 1

    if res:
        num_res = []
        data = data[ob_i-55:ob_i+1]
        for i in range(0,56,7):
            section = data[i:i+7]
            for j in range(len(number)):
                cnt = 0
                for k in range(7):
                    if section[k] == number[j][k]:
                        cnt += 1
                if cnt == 7:
                    num_res += [j]
                    break
            else:
                res = 0
                break
        if res:
            temp1 = 0
            temp2 = 0
            for i in range(7):
                if i%2:
                    temp2 += num_res[i]
                else:
                    temp1 += num_res[i]
            if (temp1*3+temp2+num_res[7]) % 10 or not (temp1+temp2+num_res[7]):
                res = 0
            else:
                res = temp1+temp2+num_res[7]
    print('#{} {}'.format(tc, res))



