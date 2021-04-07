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
            temp = [i]
            # 현재의 미생물과 같은 위치에 있는 미생물 찾기
            for j in range(i+1,len(microbes)):
                if microbes[i][0] == microbes[j][0] and microbes[i][1] == microbes[j][1]:
                    temp += [j] # 같은 위치에 있는 미생물 저장
            # 같은 위치에 있는 미생물이 존재할 때
            if len(temp) > 1:
                max_v = microbes[temp[0]][2]
                max_i = 0
                sum_micro = 0
                # 최대 미생물 수를 가지는 미생물 군 및 미생물 합 추출
                for j in range(len(temp)):
                    value = microbes[temp[j]][2]
                    if max_v < value:
                        max_v = value
                        max_i = j
                    sum_micro += value

                # 현재의 미생물 군의 이동 방향과 미생물 수 결정
                microbes[i][3] = microbes[temp[max_i]][3]
                microbes[i][2] = sum_micro

                # 합쳐진 미생물을 현재 미생물을 제외하고 미생물 리스트에서 삭제
                temp.pop(0)
                j = 0
                while j < len(temp):
                    microbes.pop(temp[j]-j)
                    j += 1
                # 인덱스 전진
                i += 1
            else:
                # 합류 미생물이 없다면 그냥 전진
                i += 1
    # 최종 시간 전진 후 미생물 잔여 수를 계산
    res = 0
    for i in range(len(microbes)):
        res += microbes[i][2]

    print('#{} {}'.format(tc, res))










