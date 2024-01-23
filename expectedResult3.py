# import random
# N = int(input())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# dice = random.randint(1, 6)
# result = 0
#
# for i in range(N):
#     if dice == 1 or dice == 2:
#         result += A[i]
#     else:
#         result += B[i]
# print(result)

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
result = 0

for i in range(N):
    result += A[i] * (1.0 / 3.0) + B[i] * (2.0 / 3.0)
print(result)