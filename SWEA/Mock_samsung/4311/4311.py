import sys
sys.stdin = open("sample_sample_input.txt")

T = int(input())

# N : 터치 가능한 숫자들의 개수 (1~10)
# O : 터치가능한 연산자들의 개수 (1~4)
# M : 최대 터치 가능한 횟수 (4~20)

# W : 원하는 숫자
for tc in range(1,T+1):
    oper_dic = {'1':'+', '2':'-', '3':'*', '4':'/'}

    def cal(input):
        stack = []
        while input:
            temp = input.pop(0)
            if temp is int:
                stack.append()


    def bfs(idex, now):
        global N, O
        if idex < N-1:

        else:


            for i in range(N):
                bfs(idex+1, now+[nums[i]])
            else:




    N, O, M = map(int, input().split())
    nums = list(map(int,input().split()))
    opers = list(input().split())
    ob_num = list(map(int,input().split()))

    # 만약 목적 수가 터치 가능한 수로 이루어져 있다면 Case1
    cnt = 0
    for i in ob_num:
        if i in nums:
            cnt += 1
    if cnt == len(ob_num):
        if cnt <= M:
            res = cnt
        else:
            res = -1
    else:
        bfs(0)
