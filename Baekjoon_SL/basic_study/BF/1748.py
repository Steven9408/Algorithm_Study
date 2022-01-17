num = int(input())

N = len(str(num))
temp = 0
res = 0
for i in range(N):
    c = 9*10**i
    temp += c
    res += (i+1) * c

res += (num - temp) * N
print(res)

