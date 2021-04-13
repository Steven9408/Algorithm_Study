import sys
sys.stdin = open("1242_input.txt")

T = int(input())

code = {(3,2,1,1):0,
        (2,2,2,1):1,
        (2,1,2,2):2,
        (1,4,1,1):3,
        (1,1,3,2):4,
        (1,2,3,1):5,
        (1,1,1,4):6,
        (1,3,1,2):7,
        (1,2,1,3):8,
        (3,1,1,2):9,}


def hexa_to_binary(chr):
    res = ''
    if ord('0') <= ord(chr) <= ord('9'):
        demi = ord(chr) - ord('0')
    else:
        demi = 10 + ord(chr) - ord('A')
    for n in range(0,4):
        res = str(demi%2) + res
        demi //= 2
    return res


def sol(str1,j_start):
    global res_list

    bits = ''
    for j in range(j_start, -1, -1):
        bits = hexa_to_binary(str1[j]) + bits

    while True:
        # 첫번째 번호를 통해 전체 사이징 조사
        for j in range(len(bits)-1, 0, -1):
            if bits[j] != '0':
                cut_j = j
                break
        else:
            break
        bits = bits[:cut_j+1]
        change = 0
        j = len(bits)
        while change < 4:
            j -= 1
            if bits[j] != bits[j-1]:
                change += 1
        number_len = len(bits) - j
        divisor = number_len//7
        bits_temp = bits[len(bits)-number_len*8:]
        bits = bits[:len(bits)-number_len*8]

        numbers = []
        ccccc= len(bits_temp)

        for i in range(0,len(bits_temp),7*divisor):
            section = bits_temp[i:i+7**divisor]
            count_bit = [0,0,0,0]
            k=0
            while section[k] == '0':
                count_bit[0] += 1
                k += 1
            while section[k] == '1':
                count_bit[1] += 1
                k += 1
            while section[k] == '0':
                count_bit[2] += 1
                k += 1
            while k < 7*divisor:
                count_bit[3] += 1
                k += 1
            for k in range(len(count_bit)):
                count_bit[k] //= divisor
            numbers += [code[tuple(count_bit)]]


        sum_code = (numbers[0] + numbers[2] + numbers[4] + numbers[6]) * 3 + numbers[1] + numbers[3] + numbers[5] + numbers[7]
        if sum_code % 10 == 0 and numbers not in res_list :
            res_list += [numbers]


for tc in range(1,T+1):
    N, M = map(int, input().split())
    res_list = []
    res = 0
    for i in range(N):
        str1 = input()
        for j in range(M-1,-1,-1):
            if str1[j] != '0':
                sol(str1,j)
                break
    for i in range(len(res_list)):
        res += sum(res_list[i])
    print('#{} {}'.format(tc, res))

