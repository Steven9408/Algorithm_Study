# E,S,M
# 1 <= E <= 15
# 1 <= S <= 28
# 1 <= M <= 19
# 1년 1 1 1
# 0이 없는 것을 주의

E ,S ,M = map(int, input().split())


e, s, m = 1, 1, 1
res = 1
while True:
    if e == E and s == S and m == M:
        break

    e += 1
    if e > 15:
        e = 1
    s += 1
    if s > 28:
        s = 1
    m += 1
    if m > 19:
        m = 1
    res += 1

print(res)
