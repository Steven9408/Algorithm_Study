import sys
sys.stdin = open("1244_input.txt")


T = int(input())

for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    income = list(map(str, input().split()))
    arry = list(map(int,income[0]))
    N = int(income[1])
    k = 0
    cnt = 0
    same = 0
    for i in range(len(arry)):
        for j in range(len(arry)):
            if arry[j] == arry[i] and i != j:
                same = 1
    while(cnt<N):
        # print(arry)
        if k >= len(arry)-1:

            if same:
                cnt += 1
                continue
            else:
                arry[-2], arry[-1] = arry[-1], arry[-2]
                cnt += 1
                continue

        max_index = k
        max_value = arry[k]
        max_indexes = []
        for i in range(k,len(arry)):
            if max_value <= arry[i]:
                max_index = i
                max_value = arry[i]

        for i in range(k,len(arry)):
            if max_value == arry[i]:
                max_indexes += [i]



        if i == k or arry[k]==arry[max_index]:
            k += 1
            continue
        elif len(max_indexes) > 1:
            candidate = list(arry[k:max_indexes[0]])
            candidate.sort()
            ssss=candidate.index(arry[k])
            arry[k], arry[max_indexes[-(ssss+1)]] = arry[max_indexes[-(ssss+1)]], arry[k]
            k += 1
            cnt += 1
            continue

        arry[max_index],arry[k] = arry[k], arry[max_index]
        k += 1
        cnt += 1
    res = "".join(map(str,arry))
    print('#{} {}'.format(test_case, res))



