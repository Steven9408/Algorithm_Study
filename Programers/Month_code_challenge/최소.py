def solution(s):
    answer = []
    N = len(s)
    for i in range(N):
        st = s[i]
        M = len(st)
        triple_i = -1
        j = 0
        while j < M:
            if j+2 < M:
                if st[j:j+3] == '111' and triple_i == -1:
                    triple_i = j
                elif st[j:j+3] == '110' and triple_i != -1:
                    obt_i = j
                    new_st = st[0:triple_i] + '110' + st[triple_i:obt_i] + st[obt_i + 3:]
                    st = new_st
                    j = triple_i + 3
                    triple_i = -1
                    continue
            j += 1
        answer.append(new_st)


    return answer
print(solution(["110011100111010"]))

# 0110110111