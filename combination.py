# 전체 탐색 풀이
# N = int(input())
# A = list(map(int, input().split()))
# M = []
#
# for i in range(N-1):
#     for j in range(1, N):
#         if A[i] == A[j] and i != j and i < j:
#             M.append([A[i], A[j]])
# print(len(M))

# n개에서 r개를 선택하는 공식을 이용한 풀이
N = int(input())
A = list(map(int, input().split()))
x = 0
y = 0
z = 0
result = 0

for i in A:
    if i == 1:
        x += 1
    elif i == 2:
        y += 1
    elif i == 3:
        z += 1

result = int((x * (x - 1) / 2) + (y * (y - 1) / 2) + (z * (z - 1) / 2))
print(result)