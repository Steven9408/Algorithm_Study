N = int(input())
res = 1
M = 10**400
start = 0
end = M
while True:
    i = (start+end)//2
    temp = i*i
    if N==temp:
        res = i
        break
    elif N > temp:
        start = i
    else:
        end = i
print(res)