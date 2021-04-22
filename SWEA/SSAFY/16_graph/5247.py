import sys
from collections import deque

sys.stdin = open("5247_input.txt")

T = int(input())


for tc in range(1, T+1):
    N, M = map(int, input().split())
    max_num = 1000000
    queue = deque([(N,0)])
    check = set()

    while queue:
        now_num, now_cnt = queue.popleft()
        if now_num == M:
            res = now_cnt
            break
        ##### +1
        temp = now_num + 1
        if temp == M:
            res = now_cnt + 1
            break
        if 1 <= temp <= max_num and temp not in check:
            queue.append((temp, now_cnt+1))
            check.add(temp)
        ##### -1
        temp = now_num - 1
        if temp == M:
            res = now_cnt + 1
            break
        if 1 <= temp <= max_num and temp not in check:
            queue.append((temp, now_cnt+1))
            check.add(temp)
        ##### *2
        temp = now_num * 2
        if temp == M:
            res = now_cnt + 1
            break
        if 1 <= temp <= max_num and temp not in check:
            queue.append((temp, now_cnt+1))
            check.add(temp)
        ##### -10
        temp = now_num - 10
        if temp == M:
            res = now_cnt + 1
            break
        if 1 <= temp <= max_num and temp not in check:
            queue.append((temp, now_cnt+1))
            check.add(temp)
    print('#{} {}'.format(tc,res))

