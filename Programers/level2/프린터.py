def solution(priorities, location):
    N = len(priorities)
    answer = 0
    while location != -1:
        if location == 0:
            now = priorities.pop(0)
            location = -1
            N = len(priorities)
            for i in range(N):
                if now < priorities[i]:
                    priorities.append(now)
                    location = N
                    break
            else:
                answer += 1

        else:
            now = priorities.pop(0)
            location -= 1
            N = len(priorities)
            for i in range(N):
                if now < priorities[i]:
                    priorities.append(now)
                    break
            else:
                answer += 1

    return answer