N = int(input())
A = list(map(int, input().split()))
min = 0

for i in range(N-1):
    min_position = i
    min_value = A[i]
    for j in range(i+1, N):
        if A[j] < min_value:
            min_position = j
            min_value = A[j]
    A[i], A[min_position] = A[min_position], A[i]

for i in range(N):
    print(A[i])

