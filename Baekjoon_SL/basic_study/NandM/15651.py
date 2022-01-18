N, M = map(int, input().split())

def dfs(l, nums):
    global visited
    if l == M:
        print(*nums)
    else:
        for i in range(1,N+1):
                dfs(l+1, nums + [i])

dfs(0, [])