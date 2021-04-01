import sys
sys.stdin = open('6019_input.txt')

T = int(input())

for tc in range(1, T+1):
    D,A,B,F = list(map(int,input().split()))
    res=D/(A+B)*F
    print('#{} {}'.format(tc,res))