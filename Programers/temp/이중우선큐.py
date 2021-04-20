
def oper(queue, oper):
    if oper[0] == 'I':
        number = int(oper[2:])
        queue.append(number)
    else:
        if queue:
            if oper[2] == '-':
                min_v = queue[0]
                min_i = 0
                for i in range(len(queue)):
                    if min_v > queue[i]:
                        min_v = queue[i]
                        min_i = i
                queue.pop(min_i)
                return queue
            else:
                max_v = queue[0]
                max_i = 0
                for i in range(len(queue)):
                    if max_v < queue[i]:
                        max_v = queue[i]
                        max_i = i
                queue.pop(max_i)
                return queue
        else:
            return

def solution(operations):
    queue = []
    for operation in operations:
        queue = oper(queue, operations)
    res =[]
    if queue:
        res += [max(queue)]
        res -= [min(queue)]
    else:
        res = [0,0]

    answer = res
    return answer

print(solution(["I 16","D 1"]))
