T = int(input())

def dfs(l,v,c):
    global res
    if l == c+1:
        if v == N:
            res += 1
    else:
        for i in range(1,4):
            dfs(l+1, v+i, c)

for tc in range(T):
    N = int(input())
    res = 0
    max_l = N

    for c in range(0, max_l):
        dfs(0, 0, c)
    print(res)


