N = int(input())
A = list(map(int, input().split()))
cnt = 0

for i in range(N):
    for j in range(i + 1, N):
        if A[i] + A[j] == 100000:
            cnt += 1
print(cnt)