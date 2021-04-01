import sys
sys.stdin = open("number_card_input.txt")

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arry = input()
    print(arry)
    cnt = [0]*10
    for i in range(N):
        cnt[int(arry[i])] += 1

    max_index = 9
    for i in range(len(cnt)):
        if cnt[max_index] <= cnt[i]:
            max_index = i

    print('#{} {} {}'.format(tc,max_index, cnt[max_index]))





