T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
   test_case_length = int(input())
   building_list = list(map(int, input().split()))
   count = 0

   for i in range(2, test_case_length - 2):
      building_height = building_list[i]
      around_max_height = 0
      for j in range(i-2, i+3):
         if j != i and around_max_height < building_list[j]:
            around_max_height = building_list[j]
      if building_height <= around_max_height:
         continue

      count += building_height - around_max_height

   print("#{} {}".format(test_case, count))