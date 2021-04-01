numbers = [-5,-4,-3,-2,-1,1,2,3,4,5]
N = 10
for i in range(1<<N):
    sum_v = 0
    for j in range(N):
        if i & (1<<j):
            sum_v = numbers[j]
