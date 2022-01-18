N, M = map(int, input().split())

visited = [False for i in range(N+1)]
def dfs(l, nums):
    global visited
    if l == M:
        print(*nums)
    else:
        for i in range(1,N+1):
            if not visited[i]:
                visited[i] = True
                dfs(l+1, nums + [i])
                visited[i] = False

dfs(0, [])