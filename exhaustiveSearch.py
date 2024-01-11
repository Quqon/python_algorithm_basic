N = int(input())
A = list(map(int, input().split()))
M = []
result = 0
cnt = 0
L = []

for i in range(N):
    if M:
        L = M
        M.clear()
    M.append(A[i])
    if len(M) == 5 and M != L:
        print(M)
        for i in M:
            result += i
        if result == 1000:
            cnt += 1
        elif result != 1000:
            i = 0
            continue
print(cnt)