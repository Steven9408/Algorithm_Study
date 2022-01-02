arr = []
arr += [input()]
arr += [input()]

N1 = len(arr[0])
N2 = len(arr[1])
if N1 > N2:
    str1 = arr[0]
    str2 = arr[1]
else:
    str1 = arr[1]
    str2 = arr[0]
    N1,N2 = N2,N1

res = 1
j = 0
for i in range(N1):
    if str1[i] == str2[j]:
        j += 1
        if j == N2:
            j = 0
        continue
    else:
        res = 0
        break
print(res)
