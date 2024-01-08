N = int(input())
A = list(map(int, input().split()))
i = 0
b = []
c = [None] * N
cnt = 0

for i in A:
    for j in range(2, i + 1):
        if i % j == 0:
            if i % (j-1) == 0 and (j-1) != 1:
                b.append(j-1)
                i = i // (j-1)
                continue
            b.append(j)
            i = i // j
        elif i % (j - 1) == 0:
            b.append(j - 1)
print(c)