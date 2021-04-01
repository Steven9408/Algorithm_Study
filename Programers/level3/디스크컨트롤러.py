def solution(jobs):
    N = len(jobs)
    check = [0] * N
    finish = [0] * N
    t = 0

    min_i = 0
    min_v = jobs[0][0]
    for i in range(N):
        if min_v > jobs[i][0]:
            min_i = i
            min_v = jobs[i][0]

    check[min_i] = 1
    finish[min_i] = jobs[min_i][0] + jobs[min_i][1]
    t = finish[min_i]

    while 0 in finish:
        indexs = []
        # 작업이 끝난 시점에서 요청이 들어와 있는 인덱스를 찾는다.
        for i in range(N):
            if not check[i] and t >= jobs[i][0]:
                indexs += [i]
        # 다음은 요청이 들어와 있는 인덱스가 있을때,
        if indexs:
            # 요청중 가장 작업시간 짧은 것을 먼저 처리할 것임
            min_i = 0
            min_v = jobs[indexs[0]][1]
            for i in range(len(indexs)):
                if min_v > jobs[indexs[i]][1]:
                    min_i = i
                    min_v = jobs[indexs[i]][1]

            check[indexs[min_i]] = 1
            finish[indexs[min_i]] = t + jobs[indexs[min_i]][1]
            t = finish[indexs[min_i]]
        else:
            # 만약 실행가능한 인원이 없다면, 제일 요청이 빠른 놈부터 처리
            min_i = 0
            min_v = jobs[0][0]
            # 제일 요청이 빠른놈 찾기
            for i in range(N):
                if min_v > jobs[i][0]:
                    min_i = i
                    min_v = jobs[i][0]

            check[indexs[min_i]] = 1
            finish[indexs[min_i]] = jobs[min_i][0] + jobs[indexs[min_i]][1]
            t = finish[indexs[min_i]]

    answer = 0
    for i in range(N):
        answer += finish[i] - jobs[i][0]

    return answer // N