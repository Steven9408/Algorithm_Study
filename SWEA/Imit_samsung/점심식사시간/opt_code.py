import sys

sys.stdin = open("input.txt")

T = int(input())


# 조합 만들기
def con(idx):
    global res
    if idx >= N_person:
        res += [step()]

    else:
        con(idx + 1)
        select[idx] = 1
        con(idx + 1)
        select[idx] = 0


# 타임 스탭을 통해 시간 구하기
def step():
    t = 0
    s0_sel = []
    s1_sel = []
    s0_queue = []
    s1_queue = []

    # 선택된 계단과 선택한 사람의 거리를 구해서 거리순으로 오름차순 정리
    for i in range(N_person):
        if not select[i]:
            dis = abs(S[0][0] - P[i][0]) + abs(S[0][1] - P[i][1])
            s0_sel += [dis]
        else:
            dis = abs(S[1][0] - P[i][0]) + abs(S[1][1] - P[i][1])
            s1_sel += [dis]

    # 시간 진전 반복문
    while True:
        t += 1

        # 계단 끝에 도착한 인원 빼주기
        if s0_queue:
            i = 0
            while i != len(s0_queue):
                if (t - s0_queue[i]) == S[0][2]:  # 현재 시간과 진입시간의 차를 통해 계단 끝에 도달했는지 판별
                    s0_queue.pop(i)  # 도착했으면 큐 리스트에서 제외
                else:
                    i += 1
        if s1_queue:
            i = 0
            while i != len(s1_queue):
                if (t - s1_queue[i]) == S[1][2]:
                    s1_queue.pop(i)
                else:
                    i += 1

        # 계단에서 대기하는 인원 스택에 넣어주기
        i = 0
        while i != len(s0_sel):
            if s0_sel[i] < t and len(s0_queue) < 3:  # 거리가 현재시간보다 작고 계단 큐 리스트의 길이에 제한이 되지 않는다면
                temp = s0_sel.pop(i)  # 사람을 sel에서 뽑아내고
                s0_queue.append(t)  # 사람을 계단에 진입시킨다.
            else:
                i += 1
        i = 0
        while i != len(s1_sel):
            if s1_sel[i] < t and len(s1_queue) < 3:
                temp = s1_sel.pop(i)
                s1_queue.append(t)
            else:
                i += 1

        if not s0_sel and not s0_queue and not s1_sel and not s1_queue:  # 모두 계단을 내려왔으면 반복문을 종료하고 시간을 리턴한다.
            break
    return t


for tc in range(1, T + 1):
    N = int(input())
    P = []
    S = []
    res = []
    for i in range(N):
        data = list(map(int, input().split()))
        for j in range(N):
            if data[j] > 1:
                S += [[i, j, data[j]]]
            elif data[j] == 1:
                P += [[i, j]]
    N_person = len(P)
    select = [0] * N_person
    con(0)
    print('#{} {}'.format(tc, min(res)))