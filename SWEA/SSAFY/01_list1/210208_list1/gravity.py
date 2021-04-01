# 낙차가 가장 큰 상자의 낙차 구하기

w = 8
boxes= [7, 4, 2, 0, 0, 6, 0, 7, 0]

drop_max = 0
for i in range(len(boxes)):
    drop = 0
    for j in range(i+1, len(boxes)):
        if boxes[i] > boxes[j]:
            drop += 1

    if drop_max < drop:
        drop_max = drop

print(drop_max)