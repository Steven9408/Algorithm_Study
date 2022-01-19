L, C = map(int, input().split())
chars = sorted(input().split())
mc = ['a', 'e', 'i', 'o', 'u']
m = []

def dfs_m(l,arr):
    global r_m
    if l == max_m:
        temp = []
        for i in range(max_m):
            temp.append(m[arr[i]])
        r_m.append(temp)

    else:
        if arr:
            a = arr[-1] + 1
        else:
            a = 0
        for i in range(a, len(m)):
            dfs_m(l+1, arr+[i])


def dfs_s(l, arr):
    global r_s
    if l == max_s:
        temp = []
        for i in range(max_s):
            temp.append(chars[arr[i]])
        r_s.append(temp)

    else:
        if arr:
            a = arr[-1] + 1
        else:
            a = 0
        for i in range(a, len(chars)):
            dfs_s(l+1, arr + [i])


i = 0
while i < len(chars):
    if chars[i] in mc:
        m.append(chars.pop(i))
        continue
    else:
        i += 1
con = []
for i in range(1, L-2+1):
    for j in range(2, L-1+1):
        if i+j == L and i <= len(m):
            con.append([i,j])
res = []
for k in range(len(con)):
    max_m = con[k][0]
    max_s = con[k][1]
    r_m = []
    r_s = []
    dfs_m(0, [])
    dfs_s(0, [])

    for i in range(len(r_m)):
        for j in range(len(r_s)):
            res.append(''.join(sorted(r_m[i] + r_s[j])))

res.sort()
for i in range(len(res)):
    print(res[i])



