A,B = list(map(int,input().split()))
temp1 = [A]
res = 0
k = 1
while temp1:
    temp2 = []
    for i in range(len(temp1)):
        value1 = temp1[i]*2
        value2 = temp1[i]*10+1
        if value1 == B or value2==B:
            res = k;
            break

        if value1 > B:
            pass
        else:
            temp2 += [value1]
        if value2 > B:
            pass
        else:
            temp2 += [value2]

    if res:
        res += 1
        break
    temp1 = list(temp2)
    k += 1
else:
    res=-1

print(res)