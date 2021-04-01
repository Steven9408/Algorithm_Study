import sys
sys.stdin = open("2806_input.txt")

T =int(input())

for tc in range(1,T+1):
    N = int(input())

    possible = [[0]*N for _ in range(N**N)]

    print(possible)

    for i in range(N):

