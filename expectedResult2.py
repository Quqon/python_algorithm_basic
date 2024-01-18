N = int(input())
A = [None] * N
for i in range(N):
    A[i] = list(map(int, input().split()))

result = 0

for j in range(N):
    result += A[j][1] // A[j][0]
print(result)