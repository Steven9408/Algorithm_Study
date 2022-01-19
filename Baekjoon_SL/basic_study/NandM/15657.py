N, M = map(int, input().split())

nums = sorted(map(int, input().split()))

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
        for i in range(a,N):
            dfs(l+1,arr+[i])
dfs(0, [])