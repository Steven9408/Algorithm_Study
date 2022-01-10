# s_list = []
# for i in range(2,M):
#     for j in range(len(s_list)):
#         if i%s_list[j] == 0:
#             break
#     else:
#         s_list.append(i)
#
# res = []
# for i in range(M,N+1):
#     for j in range(len(s_list)):
#         if i%s_list[j] == 0:
#             break
#     else:
#         s_list.append(i)
#         res.append(i)
#
# for i in range(len(res)):
#     print(res[i])

M, N = map(int, input().split())
arr = [1 for _ in range(N+1)]
for i in range(2,N+1):
    j = 1
    while i*j <= N:
        arr[i*j] += 1
        j += 1

for i in range(M,N+1):
    if arr[i] == 2:
        print(i)


