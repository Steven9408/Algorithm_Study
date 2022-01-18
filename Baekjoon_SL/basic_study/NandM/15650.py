N, M = map(int, input().split())

visited = [False for i in range(N+1)]
def dfs(l, nums):
    global visited
    if l == M:
        print(*nums)
    else:
        if nums:
            a = nums[-1]
        else:
            a = 1
        for i in range(a,N+1):
            if not visited[i]:
                visited[i] = True
                dfs(l+1, nums + [i])
                visited[i] = False

dfs(0, [])