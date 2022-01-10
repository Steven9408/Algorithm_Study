A, B = map(int, input().split())

# 최대 공약수
min_num = min([A,B])

for i in range(min_num, 0, -1):
    if A%i == 0 and B%i == 0:
        print(i)
        break
i=1
j=1
while True:
    if A*i == B*j:
        print(A*i)
        break
    else:
        if A*i > B*j:
            j += 1
        else:
            i += 1



