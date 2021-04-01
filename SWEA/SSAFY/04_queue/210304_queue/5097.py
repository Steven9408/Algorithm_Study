import sys
sys.stdin = open("5097_input.txt")

T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())

    lst = input().split()

    for i in range(M):
        temp = lst.pop(0)
        lst.append(temp)

    print('#{} {}'.format(tc,lst[0]))