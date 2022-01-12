keys = []
for _ in range(9):
    keys.append(int(input()))
res = []
res_r = []
def dfs(check, l, n):
    global res
    if l == 9:
        print(check, n)
        if n == 100 and sum(check)==7:
            res = list(check)
            return True
    else:
        if sum(check) + 1 <= 7:
            if dfs(check+[1], l+1 , n + keys[l]):
                return True
        if dfs(check+[0], l+1, n):
            return True
    return False

dfs([], 0, 0)
for i in range(len(res)):
    if res[i] == 1:
        res_r.append(keys[i])
res_r.sort()
for num in res_r:
    print(num)
