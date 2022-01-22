N = int(input())

inequals = list(input().split())

visited = [False for _ in range(10)]

def dfs(l, arr):
    global res_max, res_min
    if l == N+1:
        temp = ''
        for i in range(l):
            temp += str(arr[i])
        if int(res_max) < int(temp):
            res_max = str(temp)
        if int(res_min) > int(temp):
            res_min = str(temp)


    else:
        for i in range(10):
            if not visited[i]:
                sign = inequals[l-1]
                if sign == '<':
                    if arr[l-1] < i:
                        visited[i] = True
                        dfs(l+1, arr + [i])
                        visited[i] = False
                else:
                    if arr[l-1] > i:
                        visited[i] = True
                        dfs(l+1, arr + [i])
                        visited[i] = False

res_max = "0"*(N+1)
res_min = "9"*(N+1)

for k in range(10):
    visited[k] = True
    dfs(1, [k])
    visited[k] = False

print(res_max)
print(res_min)