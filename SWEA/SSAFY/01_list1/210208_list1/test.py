# 디버거 사용하기
# sum의 중간값을 확인하기
# step over : 함수 진입하지 않음
# step into : 함수진입
# resume : 다음 break point 까지 실행
ccc = 0
def test(a):
    global ccc
    ccc += a
    print(ccc)


for i in range(10):
    test(i)