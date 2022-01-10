N = int(input())

nums = []
for _ in range(N):
    nums.append(int(input()))
MAX = max(nums)

arr = [1 for _ in range(MAX+1)]
arr[0] = 0

for i in range(2,MAX+1):
    j = 1
    while i*j <= MAX:
        arr[i*j] += i
        j += 1

sig = [0 for _ in range(MAX+1)]
for i in range(1,MAX+1):
    sig[i] = sig[i-1] + arr[i]

for i in range(N):
    print(sig[nums[i]])