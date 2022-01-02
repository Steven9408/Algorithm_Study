def solution(genres, plays):
    N = len(genres)

    temps = set(genres)
    res = []
    dicts = {}

    for temp in temps:
        dicts[temp] = 0

    for i in range(N):
        dicts[genres[i]] += plays[i]

    dicts = sorted(dicts.items(), key=lambda x:x[1], reverse=True)
    for dict in dicts:
        temp_i = []
        # 장르 뽑기
        for i in range(N):
            if dict[0] == genres[i]:
                temp_i += [[i,plays[i]]]

        # 플레이순 내림차순
        temp_i.sort(key= lambda x:x[1], reverse=True)
        if len(temp_i) == 1:
            res += [temp_i[0][0]]
        else:
            temp_i = temp_i[0:2]
            q = [temp_i[0]]
            for i in range(1,len(temp_i)):
                if not q or temp_i[i] == q[0]:
                    q += [temp_i[i]]
                else:
                    q.sort(key=lambda x:x[0])
                    for j in range(len(q)):
                        res += [q[j][0]]
                    q = [temp_i[i]]
            q.sort(key=lambda x: x[0])
            for j in range(len(q)):
                res += [q[j][0]]
            q = [temp_i[i]]

    return res

solution(["classic", "pop", "classic", "classic", "pop",], [500, 500, 500, 500, 500])
print(solution(["classic", "pop", "classic", "classic", "pop",], [500, 500, 500, 500, 500]))