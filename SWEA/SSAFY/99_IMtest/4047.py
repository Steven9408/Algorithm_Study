import sys
sys.stdin = open("4047_input.txt")

T = int(input())

for tc in range(1,T+1):
    lst = list(' '.join(input()).split())
    pattern = {'S': 0, 'D': 1,'H': 2, 'C': 3}
    card = [[0]*14 for _ in range(4)]
    error = 0
    res = [0]*4
    for i in range(0,len(lst),3):
        index_j = int(lst[i+1])*10+int(lst[i+2])
        card[pattern[lst[i]]][index_j] += 1
        if card[pattern[lst[i]]][index_j] == 2:
            error = 1
            break
    else:
        for i in range(4):
            res[i] = 13 - sum(card[i])
    print('#{} '.format(tc),end='')
    if error:
        print('ERROR')
    else:
        print(*res)

