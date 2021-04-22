import sys
sys.stdin = open("5248_input.txt")

T = int(input())

def make_set(x):
    p[x] = x

def find_set(x):
    if p[x] == x:
        return x
    else:
        return find_set(p[x])

def union(x,y):
    p[find_set(x)] = find_set(y)


for tc in range(1, T+1):
    N, M = map(int, input().split())

    p = [0]*N
    arr = list(map(int, input().split()))
    adj = [[0]*N for _ in range(N)]

    for i in range(N):
        make_set(i)

    for i in range(0,2*M,2):
        s = arr[i]
        e = arr[i+1]
        union(s-1,e-1)
    res = []
    for i in range(N):
        res.append(find_set(i))
    print(list(range(0,N)))
    print(p)
    print(res)

    print('#{} {}'.format(tc,len(set(res))))


