keys = []
for _ in range(9):
    keys.append(int(input()))
res = []
res_r = []
def dfs(check, l, n):
    global res
    print(l)
    if l == 7:
      if n == 100:
          res = list(check)
          return True
    else:
        if n + keys[l] <= 100:
            if dfs(check+[1], l+1 , n + n + keys[l]):
                return True
        if dfs(check+[0], l+1, n):
            return True
    return False

dfs([], 0, 0)
for i in range(len(res)):
    if res[i] == 1:
        res_r.append(keys[i])
print(sorted(res_r))
