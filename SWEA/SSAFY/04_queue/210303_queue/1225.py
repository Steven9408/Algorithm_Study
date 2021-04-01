import sys
sys.stdin = open("1225_input.txt")

T = 10

for _ in range(1,T+1):
    tc = int(input())
    numbers = list(map(int, input().split()))
    N = 8
    while numbers[N-1] > 0:
        for i in range(1,6):
            temp = numbers.pop(0)
            numbers.append(temp-i)
            if numbers[N - 1] <= 0:
                numbers[N - 1] = 0
                break
    print('#{} '.format(tc),end='')
    print(*numbers)