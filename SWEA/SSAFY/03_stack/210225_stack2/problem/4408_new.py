import sys
sys.stdin = open('4408_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    students = []
    res = 0
    for i in range(N):
        students += [list(map(int, input().split()))]

    #만약 동일한 방에 가야한다면 지워버린다.
    for i in range(N-1,-1,-1):
        if students[i][0] == students[i][1]:
            students.pop()

    # students의 맴버 수가 1이나 0이면 반복문을 종료한다
    while len(students) > 1:
        i = 0 # 시작 인덱스
        check = [i] # 반복문 1회 회전 후 삭제 해야될 학생들
        route = [0]*200 # 길
        max_j = (students[i][1] - 1) // 2
        min_j = (students[i][0] - 1) // 2
        if max_j >= min_j:
            # max_j가 크거나 같을 때, min_j 부터 max_j까지 route요소를 1로
            for j in range(min_j, max_j + 1):
                route[j] += 1
            # max_j가 작을 때, max_j 부터 min_j까지 route요소를 1로
        else:
            for j in range(max_j, min_j + 1):
                route[j] += 1
        # 첫번째, 학생에 대한 route 업데이트 완료


        for k in range(i+1,len(students)):
            # 첫번째 학생과 나머지 학생들의 루트를 비교
            # 만약 첫번째 학생과 동선이 겹치지 않는다면,
            # check 리스트에 학생 인덱스를 저장하고, route를 업데이트 시킨다.
            # 만약 겹친다면, route를 이전상태로 초기화 한다.


            wrong = 0 # 동선 겹침 판단 변수
            old_route = list(route)  # 동선이 겹쳤을때, 이전상태 초기화를 위한
            max_j = (students[k][1] - 1) // 2
            min_j = (students[k][0] - 1) // 2
            if max_j >= min_j:
                for j in range(min_j, max_j + 1):
                    route[j] += 1
                    if route[j] > 1:
                        # 만약 route 요소 값이 1보다 크다면,
                        # 이는 동선이 겹친다는 것을 의미
                        route = list(old_route) # route를 이전으로 초기화
                        wrong = 1 # 동선 겹침 판단 변수 활성화
                        break # 반복문을 종료하고 새로운 k(학생인덱스)ㄱㄱ
            else:
                for j in range(max_j, min_j + 1):
                    route[j] += 1
                    if route[j] > 1:
                        route = list(old_route)
                        wrong = 1
                        break

            if not wrong:
                # 만약 wrong이 활성화 되지 않았으면 student에서 삭제할 인덱스 k를 넣어준다.
                check += [k]
        # 첫번째 학생과 다른학생의 비교를 마쳤으면
        for j in range(len(check)-1,-1,-1):
            # check에 저장된 학생들을 students에서 지운다.
            students.pop(check[j])
        # 반복문 1회 완료
        res += 1

    # 만약 students 안에 학생이 존재한다면, 이는 1명일 것이다.
    if students:
        res += 1
    print('#{} {}'.format(tc, res))

