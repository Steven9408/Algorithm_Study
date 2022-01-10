nums = []
while True:
    temp = int(input())
    if temp:
        nums.append(temp)
    else:
        break

N = max(nums)
M = 2
arr = [2 for _ in range(N+1)]
for i in range(2,N//2+1):
    j = 2
    while i*j <= N:
        arr[i*j] += 1
        j += 1
s_list = [False for _ in range(N+1)]
for i in range(2, N+1):
    if arr[i] == 2:
        s_list[i] = True

for num in nums:
    for i in range(2, num+1):
        if s_list[i] == True:
            if s_list[num - i] == True:
                print("{} = {} + {}".format(num, i, num - i))
                break


