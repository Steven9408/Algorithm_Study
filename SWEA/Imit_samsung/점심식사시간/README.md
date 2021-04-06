## 2383. 점심 식사시간

### 1. 문제 요약

- `N`: 정사각형 변의 크기, 이차원 배열 필요, 인덱스는 1부터!!

- 최대한 빠른시간!

- `P` : 사람

- `S` 계단

- 이동 완료 시간은 모든 사람들이 계단을 내려가 아래층으로 이동을 완료했을 때

- 사람들이 아래층으로 이동하는 시간은 `계단 입구까지 이동시간` +`계단을 내려가는 시간` 

  1) 계단 입구까지 이동시간

  - 사람이 현재 위치에서 계단의 입구까지 이동하는데 걸리는 시간은 다음과 같다.
    - **이동 시간(분) = | PR - SR | + | PC - SCㅣ**
    - PR,PC : 사람 P의 세로위치, 가로위치| SR,SC : 계단 입구 S의 세로위치, 가로위치

  2) 계단을 내려가는 시간

  - 계단을 내려가는 시간은 계단 입구에 도착한 후부터 계단을 완전히 내려갈 때 까지 시간
    - 계단 입구에 도착하면, 1분 후 아래칸으로 내려갈 수 있다.
    - 계단 위에는 동시에 `최대 3명 까지만` 올라갈 수 있다.
    - 이미 계단을 3명이 내려가고 있는 경우, 그 중 한 명이 계단을 완전히 내려갈 때까지 계단 입구에서 대기해야한다.
    - 계단마다 길이 K가 주어지며, 계단에 올라간 후 완전히 내려가는데 `K`분이 걸린다.

- 사람의 위치와 계단 입구의 위치 및 계단의 길이 정보가 표시된 N*N 크기의 지도가 주어질때,

- 모든 사람들이 내려가 이동이 완료되는 시간이 최소가 되는 시간을 찾아라.

- 제약 조건은 다음과 같다.

  - 시간제한 : 50개 케이스를 통과하는데 6초
  - 4<= `N` <=10
  - 1<= 사람수<=10
  - `S`의 수 = 2
  - 2<=`S` <= 10
  - 입력으로 주어지는 사람의 위치와 계단 입구의 위치는 서로 겹치지 않는다.

### 2. 풀이 전 생각

- 각 사람이 어떤 계단을 선택하는지 조합으로 표현되어야한다.

- 선택된 조합에서 시간을 전진시키며 시간을 구해야한다.

  ```
  # 최악의 시간
  (2^10)*(20+10) = 30,720
  30,720*50(문제수) = 1,536,000
  그렇게 해서 풀어도 문제는 없겠다.
  ```

- 조합을 구하는 코드와 시간을 전진시키는 코드의 분리가 필요하다.
- 시간 전진을 위한 코드는 계단 딜레이 타임을 주의해서 짜야한다.

### 3. 코드 풀이

```python
import sys
sys.stdin = open("input.txt")

T = int(input())


#조합 만들기
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
            dis = abs(S[0][0]-P[i][0]) + abs(S[0][1]-P[i][1])
            s0_sel += [[i, dis]]
        else:
            dis = abs(S[1][0] - P[i][0]) + abs(S[1][1] - P[i][1])
            s1_sel += [[i, dis]]
    s0_sel.sort(key=lambda x:x[1])
    s1_sel.sort(key=lambda x: x[1])
    
    # 시간 진전 반복문
    while True:
        t += 1
        
        # 계단 끝에 도착한 인원 빼주기
        if s0_queue:
            i = 0
            while i != len(s0_queue):
                if (t - s0_queue[i][1]) == S[0][2]: # 현재 시간과 진입시간의 차를 통해 계단 끝에 도달했는지 판별
                    s0_queue.pop(i) # 도착했으면 큐 리스트에서 제외
                else:
                    i += 1
        if s1_queue:
            i = 0
            while i != len(s1_queue):
                if (t - s1_queue[i][1]) == S[1][2]:
                    s1_queue.pop(i)
                else:
                    i += 1

        # 계단에서 대기하는 인원 스택에 넣어주기
        i = 0
        while i != len(s0_sel):
            if s0_sel[i][1] < t and len(s0_queue) < 3: # 거리가 현재시간보다 작고 계단 큐 리스트의 길이에 제한이 되지 않는다면
                temp = s0_sel.pop(i)          # 사람을 sel에서 뽑아내고
                s0_queue.append([temp[0], t]) # 사람을 계단에 진입시킨다.
            else:
                i += 1
        i = 0
        while i != len(s1_sel):
            if s1_sel[i][1] < t and len(s1_queue) < 3:
                temp = s1_sel.pop(i)
                s1_queue.append([temp[0], t])
            else:
                i += 1


        if not s0_sel and not s0_queue and not s1_sel and not s1_queue: # 모두 계단을 내려왔으면 반복문을 종료하고 시간을 리턴한다. 
            break
    return t


for tc in range(1,T+1):
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
                P += [[i,j]]
    N_person = len(P)
    select = [0]*N_person
    con(0)
    print('#{} {}'.format(tc, min(res)))
```

- 예상한 것과 같이 Brutuce 방법을 사용하니 해결했다.
- 데이터를 받아들일 때, 계단과 사람이라 판별하여 저장했다.
- 그리고 계산에 들어간다.
- 코드는 두 모듈로 나뉜다.
  - 먼저 가능한 경우의 조합을 구한다.
    - 재귀함수를 사용해 구했다.
    - 계단은 두 개 고정이니깐 0과 1로 표현했다.
    - `조합을 구할때 초기 화가 중요했다.`
  - 그 다음은 조합된 값으로 사람들이 계단을 내려오는 시간을 구했다.
    - 사람들은 각자 선택한 계단에 따라 계단 도착 시간을 구한다.
    - 계단 도착시간을 다 구했으면 정렬시키고 시간 전진 반복문에 들어간다.
    - 시간 전진 반복문은 계단 끝인원 처리, 계단에 사람 투입 순으로 진행된다.
      - 반대로 처리하게 된다면 계단이 비었을 때, 사람이 제대로 들어오지 않는다.
    - `여기에서 실수를 좀 했는데, 큐 리스트에서 데이터를 팝할 때 리스트의 인덱스 변화를 고려하지 않아 계속 오류가 났다.`
    - `팝 할때는 리스트 크기가 변하므로 for문을 사용하는게 적절하지 않다.`
    - 모든 사람이 도착했을 때, 반복문은 종료된다.
- 위의 두 가지 모듈을 통해 결과 리스트를 얻게되며 이 중 최솟값을 프린트한다.

### 4. 코드 최적화

```python
# 수정전
    # 선택된 계단과 선택한 사람의 거리를 구해서 거리순으로 오름차순 정리
    for i in range(N_person):
        if not select[i]:
            dis = abs(S[0][0]-P[i][0]) + abs(S[0][1]-P[i][1])
            s0_sel += [[i, dis]]
        else:
            dis = abs(S[1][0] - P[i][0]) + abs(S[1][1] - P[i][1])
            s1_sel += [[i, dis]]
    s0_sel.sort(key=lambda x:x[1])
    s1_sel.sort(key=lambda x: x[1])
```

```python
# 수정후
    # 선택된 계단과 선택한 사람의 거리를 구해서 거리순으로 오름차순 정리
    for i in range(N_person):
        if not select[i]:
            dis = abs(S[0][0]-P[i][0]) + abs(S[0][1]-P[i][1])
            s0_sel += [[i, dis]]
        else:
            dis = abs(S[1][0] - P[i][0]) + abs(S[1][1] - P[i][1])
            s1_sel += [[i, dis]]
```

- 처음에는 오름차순 큐의 앞 쪽부터 뺀다는 생각으로 오름차순 정리했지만 어차피 다 방문할 예정이라면 그럴필요가 없었다. 물론 오름차순 정리를 하지 않는다면 계단에 넣기 위한 사람을 판별 할 때, 리스트 전체를 후에 방문해야 한다. 하지만 정렬을 한다고 해도 그 리스트가 크게 줄어들지 않기 때문에 상관이 없다.



```python
# 수정후
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

```

- 전체적으로 필요없는 변수에 대해서 제외를 시켰다.
- 사람을 계단으로 넣기 위한 판별에 사용되는 것은 계단과의 거리 밖에 없으므로 sel 리스트에 거리만 넣는다. 
- 또, 계단 종료 판별에는 들어온 시간만 판별에 사용되기 때문에 사람 번호를 제외하고 들어온 시간만 넣어주었다.

### 5. 정리

- 시간 전진과 재귀 조합을 통해 최소값 문제를 진행했다.
- `재귀를 통한 조합을 만들때 초기화를 꼭 기억하자`
- `list.pop을 사용할 때 리스트의 크기가 변화한다는 것을 꼭 명심하자.`
- `의외로 필요하지 않은 정보들이 문제에 들어있기도 한다.`
- `모듈화를 통해 정신없는 머리를 정리해주고 디버깅 난이도를 줄인다`
