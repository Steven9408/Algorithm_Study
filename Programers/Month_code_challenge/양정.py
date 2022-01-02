def solution(numbers):
    answer = []
    N = len(numbers)
    for i in range(N):
        temp = numbers[i]
        i_n = temp
        bin_o = ''
        for j in range(16):
            if temp % 2:
                bin_o = '1' + bin_o
            else:
                bin_o = '0' + bin_o
            temp //= 2
        print(bin_o)
        k = 1
        while True:
            number = i_n + k
            bin = ''
            for j in range(16):
                if number % 2:
                    bin = '1' + bin
                else:
                    bin = '0' + bin
                number //= 2
            cnt = 0
            for j in range(16):
                if bin_o[j] != bin[j]:
                    cnt += 1
            if cnt < 3:
                print(bin)
                break
            k += 1
        answer.append(i_n + k)


    return answer

print(solution([16383]))