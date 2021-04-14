import sys
sys.stdin = open("1224_input.txt")

T = int(input())

for tc in range(1, T + 1):
    input_data = list(map(str, input().split())) #입력 데이터
    arr = list(map(int,input_data[0])) # 숫자만 분리
    M = int(input_data[1]) # 교환 횟수 분리
    N = len(arr)

    # 동일한 숫자가 있는지 파악
    same = 0
    for i in range(N):
        for j in range(N):
            if arr[j] == arr[i] and i != j:
                same = 1

    # 교환 반복문 시작
    # 리스트 앞쪽 부터 큰 값으로 채운다
    k = 0 # 기준 인덱스
    cnt = 0 # 교환 횟수
    while cnt < M:
        # 최대 정렬이 완성되었다면 현 상태를 유지해야함
        if k >= N - 1:
            # 만약 동일한 숫자가 있다면, 그 숫자들을 계속 교환
            if same:
                cnt += 1
                continue
            else:
            # 동일한 숫자가 없다면 제일 뒤의 리스트들을 바꿔준다.
                arr[-2], arr[-1] = arr[-1], arr[-2]
                cnt += 1
                continue

        # 리스트에서 제일 큰 값의 인덱스를 찾는다.
        # 인덱스는 2개 이상일 수 있다.
        max_index = k
        max_value = arr[k]
        max_indexes = []
        # k이후 값이 제일 큰 요소 찾기
        for i in range(k,N):
            if max_value <= arr[i]:
                max_index = i
                max_value = arr[i]
        # 큰 요소가 두 개 이상일 수 있음
        for i in range(k,N):
            if max_value == arr[i]:
                max_indexes += [i]


        # 만약 k 번째 자신의 값이 제일 크다면 교환하지 않는다. 컨티뉴
        if arr[k]==arr[max_index]:
            k += 1
            continue
        # k 이후에 최대값 여러개 있다면,
        # 어떤 최대 값과 교환 해야하는지 결정해야한다.
        elif len(max_indexes) > 1:
            candidate = arr[k:max_indexes[0]] # 가장 앞에있는 최대값 전까지 불러간다.
            candidate.sort() # 오름차순 정리
            k_temp = candidate.index(arr[k]) # k와 최대값 사이에 있는 리스트에서 k가 몇번째 리스트인지 판단
            if k_temp > len(max_indexes): # 만약 k_temp가 max_indexes를 넘어가면
                k_temp = len(max_indexes) - 1
            arr[k], arr[max_indexes[-(k_temp+1)]] = arr[max_indexes[-(k_temp+1)]], arr[k] # 해당 값의 뒤에서 교환해준다.
            k += 1
            cnt += 1
            continue
        # 최대값이 하나 있을때, 그냥 교환
        arr[max_index],arr[k] = arr[k], arr[max_index]
        k += 1
        cnt += 1
    res = "".join(map(str,arr))
    print('#{} {}'.format(tc, res))