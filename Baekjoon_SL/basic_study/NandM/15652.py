N, M = map(int, input().split())


def dfs(l, nums):
    if l == M:
        print(*nums)
    else:
        if nums:
            a = nums[-1]
        else:
            a = 1
        for i in range(a, N+1):
            dfs(l+1, nums + [i])

dfs(0, [])