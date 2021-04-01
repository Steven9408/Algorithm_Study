import sys
sys.stdin = open("electronic_bus_input.txt")

T = int(input())

for tc in range(1,T+1):
    K, N, M = list(map(int,input().split()))
    charge = list(map(int,input().split())) + [N]
    fuel = K-1 # 현재 연료
    cnt = 0 # 충전 횟수
    j = 0 # 충전 위치 비교 인덱스


    for i in range(1,N):
        if charge[j] == i:
            if (charge[j+1] - charge[j]) > fuel:# 충전 필요 조건 : 다음 충전소까지 거리가 현재 연료량 보다 클때
                cnt += 1
                fuel = K
                j += 1
            else:
                j += 1
        fuel += -1
        if fuel < 0: # 연료 부족으로 전진 불가
            cnt = 0
            break

    print('#{} {}'.format(tc, cnt))