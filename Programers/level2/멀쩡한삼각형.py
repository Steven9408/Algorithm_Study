def solution(w, h):
    m = h / w
    for i in range(1, w + 1):
        temp = m * i
        if temp // 1 == temp:
            y = temp
            x = i
            break
    cnt = 0
    for i in range(1, x + 1):
        y_min = round(m * (i - 1), 8)
        y_max = round(m * i, 8)
        c1 = y_max // 1
        c2 = y_min // 1
        if c1 == y_max:
            cnt += c1 - c2
        else:
            cnt += (c1 + 1) - c2

    answer = w * h - cnt * (w / x)
    return answer