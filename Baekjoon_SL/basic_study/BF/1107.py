# 0~9,+,-
# 0에서 -은 그냥 정지
now = 100
buttons = [i for i in range(10)]

N = int(input())
M = int(input())

arr = list(map(int, input().split()))
for i in range(M):
    buttons.remove(arr[i])

# 최대한 비슷한 곳으로 이동해야한다.

l = list(str(N))
temp = []
print(l)
while l:

    # 일단 앞자리를 만든다
    ele = l.pop(0)
    if ele not in arr:
        temp.append(ele)
    else:
        
