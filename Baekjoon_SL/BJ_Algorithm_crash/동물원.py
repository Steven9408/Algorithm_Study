N = int(input())
numbers = list(map(int,input().split()))
M = max(numbers)
count_list = [0]*(M+1)
possible = True
res = 1

for i in range(N):
    count_list[numbers[i]] += 1
for i in range(M+1):
    for j in range(i,M+1):
        if count_list[i] < count_list[j]:
            possible = False
            break
    if count_list[i] > 2:
        possible = False
    if possible == False:
        break

if possible:
    for i in range(M+1):
        if count_list[i] == 0:
            temp = i-1
            break
        res *= count_list[i]
    else:
        temp = M
    if count_list[temp] == 1:
        res *= 2
else:
    res = 0
print(res)