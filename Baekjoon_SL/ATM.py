N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
res = 0
for i in range(N):
    for j in range(0,i+1):
        res += numbers[j]
print(res)