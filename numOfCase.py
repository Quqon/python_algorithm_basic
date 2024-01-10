N = int(input())
A = list(map(int, input().split()))
M = []
result = []

for i in range(N-1):
    for j in range(1, N):
        if A[i] + A[j] <= 500:
            M.append([A[i],A[j]])

for v in M:
    if v not in result:
        result.append(v)
print(len(result))
