def solution(numbers):
    answer = []
    N = len(numbers)
    M = 50
    for i in range(N):
        number = numbers[i]
        temp = number
        bin_o = ''
        for j in range(M):
            if temp % 2:
                bin_o = '1' + bin_o
            else:
                bin_o = '0' + bin_o
            temp //= 2
        for j in range(M):
            if bin_o[M-j-1] == '0':
                idx = M-j-1
                break
        if idx == M-1:
            answer.append(number+1)
        else:
            res = 0
            new_bin = ''
            for j in range(M):
                if j == idx:
                    new_bin += '1'
                elif j == idx+1:
                    new_bin += '0'
                elif idx + 1 < j:
                    new_bin += '1'
                else:
                    new_bin += bin_o[j]
            for j in range(M):
                res += int(new_bin[j])*2**(M-j-1)
            answer.append(res)



    return answer

print(solution([7]))
