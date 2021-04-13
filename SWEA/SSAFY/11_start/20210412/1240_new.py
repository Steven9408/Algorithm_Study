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
    arr = []
    # 행을 받아와서 1이 있는 행의 인덱스값 추출
    for i in range(N):
        arr += [list(map(int, ' '.join(input()).split()))]
        if 1 in arr[i]:
            ob_i = i

    # 사용할 행만 따로 뽑기
    data = list(arr[ob_i])

    # 역순으로 방문하여 1이되는 열 인덱스 파악
    for i in range(M-1,-1,-1):
        if data[i] == 1:
            ob_i = i
            break


    # 숫자 섹션을 나누어서 암호숫자와 대비, 숫자 찾기
    num_res = []
    data = data[ob_i-55:ob_i+1] # 해당 인덱스 추출
    for i in range(0,56,7):
        section = data[i:i+7] # 섹션 뽑기
        for j in range(len(number)): # 암호숫자 비교
            cnt = 0
            for k in range(7):
                if section[k] == number[j][k]:
                    cnt += 1
            if cnt == 7: # 완전히 일치하면 저장
                num_res += [j]
                break

    # 암호 유효성 판별
    temp1 = 0 # 홀수자리 합
    temp2 = 0 # 짝수자리 합
    for i in range(7):
        if i % 2:
            temp2 += num_res[i]
        else:
            temp1 += num_res[i]
    if (temp1*3+temp2+num_res[7]) % 10 or not (temp1+temp2+num_res[7]):
        res = 0
    else:
        res = temp1+temp2+num_res[7]
    print('#{} {}'.format(tc,res))
