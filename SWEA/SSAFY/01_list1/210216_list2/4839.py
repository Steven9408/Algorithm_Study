import sys
sys.stdin = open("4839_input.txt")

T = int(input())

for tc in range(1,T+1):
    P,Pa,Pb = map(int, input().split())


    P_end = P
    P_start = 1
    cnt_A = 0
    while P_start != P_end-1:
        cnt_A += 1
        P_mid = (P_start+P_end)//2;
        if Pa < P_mid:
            P_end = P_mid
        elif Pa >P_mid:
            P_start = P_mid
        else:
            break;

    P_end = P
    P_start = 1
    cnt_B = 0
    while P_start != P_end-1:
        cnt_B += 1
        P_mid = (P_start + P_end) // 2;
        if Pb < P_mid:
            P_end = P_mid
        elif Pb > P_mid:
            P_start = P_mid
        else:
            break;
    if cnt_A < cnt_B:
        res = 'A'
    elif cnt_B < cnt_A:
        res = 'B'

    else:
        res = '0'
    print('#{} {}'.format(tc,res))
