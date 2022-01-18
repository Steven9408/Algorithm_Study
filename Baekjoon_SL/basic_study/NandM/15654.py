N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

visited = [False for _ in range(N)]

def dfs(l, arr):
    if l == M:
        print(*arr)
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                dfs(l+1, arr+[nums[i]])
                visited[i] = False

dfs(0, [])
