def solution(participant, completion):
    participant.sort(reverse=True)
    completion.sort(reverse=True)
    while completion:
        if participant[-1] == completion[-1]:
            participant.pop(-1)
            completion.pop(-1)
        else:
            break
    answer = participant[-1]

    return answer