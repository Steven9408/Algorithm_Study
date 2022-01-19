N , M = map(int, input().split())

nums = sorted(list(map(int, input().split())))

def dfs(l, arr):
    if l == M:
        temp = []
        for i in range(M):
            temp.append(nums[arr[i]])
        print(*temp)
    else:
        for i in range(0,N):
            dfs(l+1, arr + [i])

dfs(0, [])