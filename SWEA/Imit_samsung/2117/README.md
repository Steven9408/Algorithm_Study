## 2382. 미생물 격리

### 1. 문제 요약

- `N*N` 크기의 도시에 홈 방범 서비스 제공
- 마름 모형태의 영역에서 제공
- 서비스 영역`K` 가 커질 수록 운영 비용이 커진다.
- 운영비용 = K*K + (K-1)(K-1) 
- 도시영역을 벗어나도 운영비용은 감소하지 않는다.
- 집들은 `M`의 비용을 지불 할 수 있다.
- 회사는 손해를 보지 않는 한 최대한 많은 집에 서비스를 제공하려고한다.
- 제약사항은 다음과 같다.
  - 시간제한 : 15초
  - 5<= N <= 20
  - 1<= M <= 20

### 2. 풀이 전 생각

- 손해를 보지 않으면서 최대한 많은 서비스 제공을 해야한다.

- `두개의 영역으로 만들 수는 없다.`

- 결국 결정해야하는 것은 K와 서비스 위치일 것이다.

- N이 짝수일때 K<=N+1, N이 홀 수 일 때, K<=N, 통합하면 K<= N

  ```
  시간 제한 검사
  N = 20 이면, 1<=K<=20
  N*N*N*(2*N**2-2*N+1) = 8000*(800-40+1) = 3억
  Brute Force를 써도 괜찮을 것 같다.
  ```

- 서비스 중심지를 선택하고, 이익을 계산 하여 필요한 값을 뽑고,

- 그 중 최대 값을 도출한다. 

- 단 여기서 좋은 점은 운용비용이 애초에 음수가 되는 K를 판별 할 수 있다.

  ```
  도시의 집의 개수가 n이라면
  n*M > 운영비용
  이를 이용해 K값에 제한을 둘 수 있다.
  ```

### 3. 코드

```python
import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    res = 0
    N_house = 0
    for i in range(N):
        data = list(map(int, input().split()))
        arr += [data]
        for j in range(N):
            if data[j]:
               N_house += 1

    # max_k 결정
    max_k = -1
    for i in range(N+2):
        if N_house*M >= i*i+(i-1)*(i-1):
            max_k = i

    for k in range(1,max_k+1):
        cost = k*k+(k-1)*(k-1)
        for i in range(N):
            for j in range(N):
                cnt = 0
                for i_s in range(-k+1,1):
                    for j_s in range(-i_s-k+1,(k+i_s-1)*2+1-i_s-k+1):
                        i_abs = i_s + i
                        j_abs = j_s + j
                        if (0 <= i_abs < N) and (0 <= j_abs < N) and arr[i_abs][j_abs] == 1:
                            cnt += 1

                for i_s in range(1,k):
                    for j_s in range(-k+i_s+1,k+k-1-2*i_s-k+i_s+1):
                        i_abs = i_s + i
                        j_abs = j_s + j
                        if (0 <= i_abs < N) and (0 <= j_abs < N) and arr[i_abs][j_abs] == 1:
                            cnt += 1
                if cnt*M >= cost and res < cnt:
                    res = cnt

    print('#{} {}'.format(tc,res))
```

- max_k 는 이차 함수의 부등식에 의해 k = 0.5 이상에서 상승한다.
  - 때문에 k값을 증가시키며 손해를 보지 않는 최대 k 값을 먼저 구했다.
  - 여기서 최대 k 값의 제한은 N이 짝수일때 N+1을 기준으로, 서비스 구역이 전체 N을 덮을 때로 지정했다.
- 이후 k를 1부터 증가시키며 서비스 중심(i,j)를 기준으로 주변을 탐색했다.
  - 다이아몬드 인덱스를 만들기 위해서 서비스 중심점 주변으로 인덱스를 구했고, 이를 중심점 좌표에 더하여 절대 좌표를 구했다.
  - 만약 해당 절대 인덱스에 집이 존재한다면 카운팅한다.
  - 이윤이 0이상 이고 res보다 cnt 가 크다면 저장한다.
- 최대 서비스 제공 집 개수를 프린트한다.

### 4. 코드 최적화

```python
# 수정후
import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    house_list = []
    res = 0
    N_house = 0
    for i in range(N):
        data = list(map(int, input().split()))
        arr += [data]
        for j in range(N):
            if data[j]:
                N_house += 1
                house_list += [[i,j]] #2.수정# 집 리스트를 받아온다.

    # max_k 결정
    max_k = -1
    for i in range(N+2):
        if N_house*M >= i*i+(i-1)*(i-1):
            max_k = i

    for k in range(max_k,0,-1): #1.수정# k를 최대부터 시작한다.
        cost = k*k+(k-1)*(k-1)
        for i in range(N):
            for j in range(N):
                cnt = 0
                for c in range(N_house): #2.수정# 중심점에서 서비스 지점 모두를 방문하는 것이
                    ## 아니라 모든 집들을 방문해서 서비스 지점 내에 있는지 확인한다.
                    dis = abs(i-house_list[c][0]) + abs(j-house_list[c][1])
                    if dis < k:
                        cnt += 1
                if cnt*M >= cost and res < cnt:
                    res = cnt
        if res:
            break

    print('#{} {}'.format(tc,res))
```

- 문제의 목적이 손해가 나지 않으면서 최대한 많은 서비스 수혜자를 만드는 것이기 때문에, 전체 조사는 필요가 없다.
- 예를들어 k1<k2 라면 k1이 k2 보다 많은 수혜자를 만들어 내는 것은 불가능하다.
- `때문에 #1.수정#과 같이 역순으로 방문하여, 손해가 나지 않는 최대 수혜를 구한다면 이후 k가 더 작아졌을때 수혜 인원은 구할 필요가 없다.`
  - 위의 1.수정 을 이용하니 속도가 30% 정도 빨라졌다.
- 2차원 다이아몬드 방문 인덱스를 만들기 위해 많은 고생을 했는데, 그럴 필요가 없었다.
  - 중심점과 집 사이의 거리를 이용하면 다이아몬드 인덱스 필요없이 구할 수 있었다.
  - 이는 k가 일정부분 커졌을 때, 많은 지점 방문을 요구하게 되는데, 상대적으로 집의 개수가 작기 때문에 더 작은 수의 방문을 필요로 한다. 때문에 속도가 20% 정도 높혀졌다.

### 5. 정리

- `문제의 조건에 따라서 방문 순서를 달리하는 것이 속도 향상에 큰 도움이 된다.`
- `방문 횟수를 줄이는 것에 큰 관심을 가지자`