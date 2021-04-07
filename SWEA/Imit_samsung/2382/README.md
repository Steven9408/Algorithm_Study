## 2382. 미생물 격리

### 1. 문제 요약

- 정사각형 구역 : `N*N`

- 가장자리에는 특수한 약품이 칠해진다.

  - 최초 각 미생물 군집의 위치, 미생물 수, 이동방향이 주어진다.
  - 각 군집들은 `1시간`마다 이동방향에 있는 다음 셀로 이동한다.
  -  미생물 군집이 이동 후 약품이 칠해진 셀에 도착하면 군집 내 미생물의 절반이 죽고 이동방향이 반대로 바뀐다.
    - 살아남은 미생물 수 = 원래 미생물 수를 2로 나눈후 소수점 이하를 버림
  - 이동 후 두 개 이상의 군집이 한 셀에 모이는 경우 군집들이 함쳐지게 된다.
    - 합쳐진 군집의 미생물 수는 군집들의 미생물 수의 합이며, 이동방향은 군집들 중 미생물 수가 가장 많은 군집의 이동방향이 된다.
    - `합쳐지는 군집의 미생물 수가 같은 경우는 주어지지 않는다.`
  - `M` 시간 동안 이 미생물 군집들을 격리하였다. `M ` 시간 후 남아 있는 미생물의 총합을 구하여라.

- 제약사항

  - 시간제한 : 50개의 테스트 케이스를 10초에 통과
  - 5<= `N` <= 100
  - `K` : 최초 배치되어 있는 미생물 군집의 개수, 5<= `K` <= 1,000
  - 격리 시간 `M`, 1< `M` < 1,000
  - 초기에 동일한 위치 배치는 없고, 가장자리에도 배치되지 않는다.
  - 1<= 미생물 수 <= 10,000
  - 이동방향은 상,하,좌,우

  ```
  최악의 시간 계산
  일단 M 시간 동안의 시간전진이 필요하고
  이 시간 동안 미생물 K 개가 다 존재할 수 있다.
  만약 로직을 어떻게 설계하느냐에 따라 다르겠지만,
  M*K*N*N*T = 1000*1000*100*100*50 = 5억
  시간이 부족한 문제는 없을 것으로 예상한다.
  ```

  

### 2. 풀이 전 생각

- 시간 전진을 통해 미생물 군집을 배치한다.
- 배치가 끝나면 각 미생물 군집을 방문해서 현재 상황을 파악한다.
  - 미생물 군집이 가장자리에 방문했을때, 군집 데이터의 방향을 변화시키고 미생물 수를 반으로 감소시킨다.
  - 미생물 군집이 합쳐졌을때
    - 먼저 한 장소에 여러 군집이 모여있는 경우를 판별해야한다.
      - 전체 위치 공간을 참조하여 위치한 미생물 수를 판별할 수 있겠지만, 이경우 K*N^2의 시간이 든다.
      - 이보다 기준점을 정해놓고, 미생물 끼리의 관계를 파악하는 것이 더 빠를 수 있겠다.(K*K)
    - 만약 같다면 이 군집중 최대의 미생물을 구하고 하나로 합치는 과정이 필요하다.

### 3. 코드 풀이

```python
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
```



### 4. 코드 최적화

```python
# 수정전
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
```

```python
# 수정후
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
```

- for문을 통해서 현재 타겟이 되는 미생물 군과 나머지 미생물 군을 비교하게 되는데 중복되는 반복문이 많아서 이를 수정했다.

### 5. 정리

- 시간 전진을 통해 문제를 해결했다.
- 단순히 프로세스만 진행하는 문제라 그리 어렵지는 않았다.
- `하지만 역시나 실수는 pop을 해주는 경우에 발생했다.`
- `생각보다 코드를 짜는데 오랜시간이 걸렸다. 시간을 조금 더 줄일 필요가 있다.`
