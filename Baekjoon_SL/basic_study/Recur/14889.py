N = int(input())

plane = []
for i in range(N):
    plane.append(list(map(int, input().split())))



def dfs(l,arr, a, b, cnt_a, cnt_b):
    global res
    if N == l:
        print(arr)
        print(a,b)
        if res > abs(a-b):
            res = abs(a-b)
    else:
        if cnt_a < N//2:
            # a팀
            temp = 0
            for i in range(N):
                if arr[i] == 1:
                    temp += plane[l][i]
                    temp += plane[i][l]
            arr[l] = 1
            dfs(l+1, list(arr), a+temp, b, cnt_a+1, cnt_b)
            # arr[l] = 0
        if cnt_b < N//2:
            # b팀
            temp = 0
            for i in range(N):
                if arr[i] == 2:
                    temp += plane[l][i]
                    temp += plane[i][l]
            arr[l] = 2
            dfs(l+1, list(arr), a, b+temp, cnt_a, cnt_b+1)
            # arr[l] = 0

c = [0 for _ in range(N)]
res = 99999999999999999999999999999999
dfs(0, c, 0, 0, 0, 0)
print(res)