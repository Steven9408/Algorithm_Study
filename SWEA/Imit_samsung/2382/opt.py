import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())

    # 세로위치, 가로위치, 미생물 수, 이동방향
    microbes = [list(map(int, input().split())) for _ in range(K)]
    dr = [0,-1, 1, 0, 0]
    dc = [0, 0, 0, -1, 1]

    for t in range(1,M+1):
        # 위치 최신화
        N_micro = len(microbes)
        # 위치 이동 벡터를 통해 각 미생물 군의 위치 이동
        for i in range(N_micro):
            microbes[i][0] += dr[microbes[i][3]]
            microbes[i][1] += dc[microbes[i][3]]

        # 경계점 검출 : 경계에 들어가는 미생물 처리
        i = 0

        while i<len(microbes):
            # 상부 접근
            if microbes[i][0] == 0:
                microbes[i][3] = 2
            # 하부 접근
            elif microbes[i][0] == N-1:
                microbes[i][3] = 1
            # 좌측 접근
            elif microbes[i][1] == 0:
                microbes[i][3] = 4
            # 우측 접근
            elif microbes[i][1] == N-1:
                microbes[i][3] = 3
            # 접근 상황이 아니라면 패스
            else:
                i += 1
                continue
            # 접근 한 미생물은 반감시켜주고
            microbes[i][2] //= 2
            # 반감했을 때, 0이되면 삭제시켜준다. 삭제 후 인덱스는 변화 안시켜줌
            if microbes[i][2] == 0:
                microbes.pop(i)
            # 삭제 미생물 군 없으면 인덱스 전진
            else:
                i += 1

        # 합류점 검출 : 함류하여 미생물이 합쳐지는 곳 처리
        i = 0
        while i < len(microbes):
            delete_list = []
            max_v = microbes[i][2]
            max_i = i
            # 현재의 미생물과 같은 위치에 있는 미생물 찾기 및 데이터 처리
            for j in range(i+1,len(microbes)):
                if microbes[i][0] == microbes[j][0] and microbes[i][1] == microbes[j][1]:
                    delete_list += [j]
                    temp = microbes[j][2]
                    if temp > max_v:
                        max_i = j
                        max_v = temp
                    microbes[i][2] += temp
            microbes[i][3] = microbes[max_i][3]

            # 겹치는 부분 삭제 진행
            j = 0
            while j < len(delete_list):
                microbes.pop(delete_list[j]-j)
                j += 1
            i += 1

    # 최종 시간 전진 후 미생물 잔여 수를 계산
    res = 0
    for i in range(len(microbes)):
        res += microbes[i][2]
    print('#{} {}'.format(tc, res))
