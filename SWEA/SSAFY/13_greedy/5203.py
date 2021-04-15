import sys
sys.stdin = open("5203_input.txt")

T = int(input())

def find_run(arr):
    N = 10
    cnt = 0
    run = False
    run_idexes= []
    for i in range(N):
        if arr[i]:
            cnt += 1
            run_idexes.append(i)
        else:
            cnt = 0
            run_idexes = []
        if cnt == 3:
            run = True
            break
    if run:
        for i in range(len(run_idexes)):
            arr[run_idexes[i]] -= 1
    return run, arr

def find_triple(arr):
    N = 10
    triple = False
    for i in range(N):
        if arr[i] >= 3:
            triple = True
            arr[i] -= 3
            break
    return triple, arr


for tc in range(1, T+1):
    data = list(map(int, input().split()))
    N = len(data)
    player = [[0] * 10 for _ in range(2)]
    res = 0
    who_win = [0,0]
    # 처음 들어온 세개의 카드로 먼저 판별
    for i in range(0,4,2):
        player[0][data[i]] += 1
        player[1][data[i+1]] += 1

    else:
        for i in range(4,N,2):
            player[0][data[i]] += 1
            player[1][data[i + 1]] += 1

            temp = False
            who_win[0], player[0] = find_run(player[0])
            temp, player[0] = find_triple(player[0])
            if temp:
                who_win[0] = temp

            if who_win[0]:
                res = 1
                break

            temp = False
            who_win[1], player[1] = find_run(player[1])
            temp, player[1] = find_triple(player[1])
            if temp:
                who_win[1] = temp

            if who_win[1]:
                res = 2
                break


    print('#{} {}'.format(tc, res))









