from collections import deque
N = int(input())
times = []
pays = []
for i in range(N):
    t, p = map(int,input().split())
    times.append(t)
    pays.append(p)

q = deque()
# 현재날, 잔여일, 총페이
q.append([1,0,0])
q.append([1, times[0]-1, pays[0]])

res = 0
while q:
    nd, rd, sp = q.popleft()
    if nd == N:
        if rd == 0 and res < sp:
            res = sp
        continue
    elif rd != 0:
        q.append([nd+1, rd-1, sp])
    else:
        # 일 추가하기
        q.append([nd + 1, times[nd]-1, sp+pays[nd]])
        # 일 하지않기
        q.append([nd+1, 0, sp])

print(res)