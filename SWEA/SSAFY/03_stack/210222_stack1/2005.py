import sys
sys.stdin = open("2005_input.txt")

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    # 출력할 배열 선언
    # N*N 크기
    arr = [[0]*N for _ in range(N)]
    print('#{}'.format(tc))

    # 행은 0부터 n-1까지, 열은 0부터 i까지 계산하여 출력
    for i in range(N):
        for j in range(i+1):
            if j == 0 or i == j:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j] + arr[i-1][j-1]
            print(arr[i][j],end=' ')
        print()


