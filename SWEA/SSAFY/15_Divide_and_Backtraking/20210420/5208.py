import sys
sys.stdin = open("5208_input.txt")

T = int(input())

def dfs(idex,fuel,cnt):
    global min_c

    if idex == N-1:
        if min_c > cnt:
            min_c = cnt
    else:
        # 최소 카운트 보다 작을때만 실시
        if cnt <= min_c:
            # 연료가 남아 있을때만 충전 안하고 전진
            if fuel > 0:
                dfs(idex+1,fuel-1,cnt)
            fuel = stations[idex]
            dfs(idex+1, fuel-1,cnt+1)


for tc in range(1, T+1):
    data = list(map(int, input().split()))
    N = data[0]
    min_c = N-1
    stations = data[1:N]
    dfs(1,stations[0]-1,0)
    print('#{} {}'.format(tc, min_c))

