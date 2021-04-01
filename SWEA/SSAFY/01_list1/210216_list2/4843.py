import sys
sys.stdin = open("4843_input.txt")

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    numbers = list(map(int,input().split()))
    cnt = 0
    for i in range(0,N,2):
        max_index = i
        max_value = numbers[max_index]
        for j in range(i,N):
            if numbers[j] > max_value:
                max_index = j
                max_value = numbers[j]
        numbers[i], numbers[max_index] = numbers[max_index], numbers[i]
        min_index = i+1
        min_value = numbers[min_index]
        for j in range(i+1,N):
            if numbers[j] < min_value:
                min_index = j
                min_value = numbers[j]

        numbers[i+1],numbers[min_index] = numbers[min_index], numbers[i+1]
        cnt += 2
        if cnt >= 10:
            break
    res = numbers[0:10]
    print('#{} '.format(tc),end='')
    print(*res)


