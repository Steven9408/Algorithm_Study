import sys
sys.stdin = open("5174_input.txt")

T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())
    lst = list(map(int, input().split()))

    queue = [N]
    cnt = 1

    while queue:
        value = queue.pop(0)
        for i in range(E):
            if lst[2*i] == value:
                cnt += 1
                queue.append(lst[2*i+1])
    print('#{} {}'.format(tc, cnt))