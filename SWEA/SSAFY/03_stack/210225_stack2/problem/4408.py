import sys
sys.stdin = open('4408_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    students = []
    check = [0]*N
    select = []
    max_cnt = 0
    def powerset(idx):
        if idx == N:
            # 최종적인 부분집합 생성 완료
            cnt = 0
            for i in range(N):
            # 부분집합의 원소 갯수 파악
                cnt += check[i]
            if max_cnt < cnt:
            # 만약 현재까지 만들어진 부분집합 개수보다 많다면,
            # 부분 집합을 저장한다.
                max_cnt = cnt
                select = list(check)
            return

        check[idx] = 1
        if route_check(idx):
            powerset(idx+1)
        check[idx] = 0
        powerset(idx+1)

    def route_check(idx):
        # 현재 만들어진 부분집합이 idx+1 = 1 일떄 동선이 겹치는지 판별
        route = [0]*200
        for i in range(idx+1):
            print(i)
            if check[i] == 1:
                max_j = (students[i][1]-1)//2
                min_j = (students[i][0]-1)//2
                if max_j >= min_j:
                    for j in range(min_j,max_j+1):
                        route[j] += 1
                else:
                    for j in range(max_j+1,min_j+1):
                        route[j] += 1
        for i in range(len(route)):
            if route[i] > 1:
                return False
        return True



    for i in range(N):
        students += [list(map(int, input().split()))]
    powerset(0)
    print(select)

