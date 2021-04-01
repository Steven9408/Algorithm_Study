import sys
sys.stdin = open("4880_input.txt")

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    def tournament(start,end):
        if start == end:
            return start
        elif end - start == 1:
            if (lst[start] > lst[end]) or lst[start] == lst[end]:
                if lst[start] == 3 and lst[end] == 1:
                    return end
                return start
            else:
                if lst[end] == 3 and lst[start] == 1:
                    return start
                return end
        else:
            res1 = tournament(start,(start+end)//2)
            res2 = tournament((start + end)//2+1, end)
            if (lst[res1] > lst[res2]) or lst[res1] == lst[res2]:
                if lst[res1] == 3 and lst[res2] == 1:
                    return res2
                return res1
            else:
                if lst[res2] == 3 and lst[res1] == 1:
                    return res1
                return res2
    res = tournament(0,N-1)
    print('#{} {}'.format(tc,res+1))



