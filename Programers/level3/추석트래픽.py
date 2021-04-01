def solution(lines):
    # 11-12 시
    # 14-15 분
    # 17-18 초
    # 20-22 0.초
    # 24-끝 : 몇초동안(s 포함)
    N = len(lines)
    time_line = []
    cut_time = [0]
    answer = 0

    for i in range(N):
        h = int(lines[i][11:13])
        m = int(lines[i][14:16])
        s = int(lines[i][17:19])
        u_s = float(lines[i][20:23]) * 0.001
        inter = float(lines[i][24:-1])
        f_time = (h * 60 + m) * 60 + s + u_s
        s_time = round(f_time - inter + 0.001, 4)
        time_line += [[s_time, f_time]]
        cut_time += [s_time, f_time]
    cut_time = list(set(cut_time))
    cut_time.sort()
    M = len(cut_time)
    cnt_list = [0] * M

    for i in range(0, M):
        cnt = 0
        for j in range(N):
            if ((cut_time[i] > time_line[j][0]) and (cut_time[i] > time_line[j][1])) or (
                    (cut_time[i] + 0.9999 < time_line[j][0]) and (cut_time[i] + 0.9999 < time_line[j][1])):
                pass
            else:
                cnt += 1
        if answer < cnt:
            answer = cnt
        cnt_list[i] = cnt

    return answer