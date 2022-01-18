N, M = map(int, input().split())

nums = sorted(list(map(int, input().split())))

visited = [False for _ in range(N)]

def dfs(l, arr):
    if l == M:
        temp = []
        for i in range(M):
            temp.append(nums[arr[i]])
        print(*temp)
    else:
        if arr:
            a = arr[-1]
        else:
            a = 0
        for i in range(a, N):
            if not visited[i]:
                visited[i] = True
                dfs(l+1, arr+[i])
                visited[i] = False

dfs(0, [])