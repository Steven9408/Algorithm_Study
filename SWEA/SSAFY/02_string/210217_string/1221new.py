import sys
sys.stdin = open("1221_input.txt")
T = int(input())
def convert(word):
    numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    for i in range(10):
        if word == numbers[i]:
            return i
numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for test_case in range(1, T + 1):
    input_data = input().split()
    N = int(input_data[1])
    words = input().split()
    cnt = [0]*10
    res = []
    for i in range(N):
        cnt[convert(words[i])] += 1
    for i in range(10):
        res += [numbers[i]] * cnt[i]
    print('#{}'.format(test_case))
    print(*res)

