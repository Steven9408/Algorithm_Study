import sys
sys.stdin = open("4873_input.txt")

T = int(input())

for tc in range(1,T+1):
    str1 = input()
    stack = []
    N = len(str1)
    # 역순으로 구성되어 있는 stack 제작
    for i in range(N):
        stack += [str1[N-i-1]]

    while True:
        # 반복문 시작에서 스택 길이 측정
        s_len = len(stack)

        # 임시 저장 스택 생성, 꺼낸 순서대로 저장해둔다.
        stack_temp = []
        # 만약 스택의 길이가 1이면 반복문 종료
        if s_len == 1:
            break

        # 첫번째 비교 대상 먼저 생성
        stack_temp += [stack.pop()]

        # 스택 길이만큼 반복문을 돌면서 하나씩 꺼내어서 이전 값과 비교해 본다.
        for i in range(len(stack)):
            top = stack.pop()# 현재 꺼낸 값

            # 현재 꺼낸 값과 임시 스택의 마지막 값이 같다면
            if top == stack_temp[-1]:
                # 임시 스택의 값들을 순차적으로 넣어준다. 임시스택의 마지막에 저장된 값은 제외 시킨다.
                # 그리고 임시 저장소 값들을 동시에 빼준다.
                # 동일 문자열 단축이 한 번 일어났으니깐 반복문은 처음으로 돌아간다.
                stack_temp.pop()
                for j in range(len(stack_temp)):
                    stack.append(stack_temp.pop())
                break
            # 비교한 현재 값을 임시스택에 추가시켜준다.
            stack_temp += [top]
        # 만약 반복문이 성공적으로 마무리 되었다면, 임시 스택에 있는 값들을 다시 스택으로 넣어준다.
        else:
            for j in range(len(stack_temp)):
                stack.append(stack_temp.pop())

        # 반복문 진행하면서 아무런 스택의 변화가 없으면 반복문을 종료한다.
        e_len = len(stack)
        if s_len == e_len:
            break
    print('#{} {}'.format(tc,len(stack)))
