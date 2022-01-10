N = int(input())

nums = list(map(int, input().split()))
cnt = 0
for i in range(N):
    if nums[i] == 1:
        continue
    for j in range(2,nums[i]//2+1):
        if nums[i]%j == 0:
            break
    else:
        cnt += 1
print(cnt)