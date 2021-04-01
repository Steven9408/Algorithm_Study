T = int(input())

for tc in range(1,T+1):
    N = int(input())
    numbers = list(map(int, input().split()))


    for i in range(N):
        min_number = numbers[i]
        min_index = i
        for j in range(i,N):
            if min_number > numbers[j]:
                min_index = j
                min_number = numbers[j]
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

    print('#{} '.format(tc),end='')
    print(*numbers)
