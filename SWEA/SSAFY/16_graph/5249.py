import sys
sys.stdin = open("5249_input.txt")

T = int(input())
def find_set(x):
    if p[x] == x:
        return x
    return find_set(p[x])

def union(x,y):
    p[find_set(y)] = find_set(x)


for tc in range(1, T+1):
    V, E = map(int, input().split())
    p = []
    for i in range(V+1):
        p.append(i)

    inp = []
    for i in range(E):
        inp.append(list(map(int, input().split())))
    inp.sort(key=lambda x:x[2])

    res = 0
    for i in range(E):
        s = inp[i][0]
        e = inp[i][1]
        if find_set(s) == find_set(e):
            continue
        union(s,e)
        res += inp[i][2]


    print('#{} {}'.format(tc, res))






