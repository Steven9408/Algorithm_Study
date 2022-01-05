def solution(stones, k):
    def dfs(l, arry, sol):
        global answer
        if l == max_M:
            # print(sol)
            for i in range(len(arry)):
                if arry[i] == k:
                    answer = list(sol)
                    return True

        else:
            for i in range(len(arry)-1,-1,-1):
                now = list(arry)
                wrong = False
                now[i] += 2
                for j in range(len(now)):
                    now[j] -= 1
                    if now[j] < 0:
                        wrong = True
                        break
                if wrong:
                    continue
                else:
                    ans = dfs(l+1, list(now), sol+[i])
                    if ans:
                        return True
        return False

    N = len(stones)

    if N == 2:
        if sum(stones) == k:
            res = ""
            cn = min(stones)
            if stones[0] > stones[1]:
                for i in range(cn):
                    res += "0"
            else:
                for i in range(cn):
                    res += "1"
            return res

        else:
            return "-1"

    temp = (sum(stones)-k) % (N-2)

    if temp != 0:
        return "-1"
    max_M = (sum(stones)-k) // (N-2)
    if max_M <= 0:
        return "-1"

    dfs(0, stones, [])

    answer2 = ""
    for i in range(len(answer)):
        answer2 += str(answer[i])

    return answer2


# print(solution([1,3,2],6))
print(solution([4,2,2,1,4],1))
# print(solution([5,7,2,4,9],20))
