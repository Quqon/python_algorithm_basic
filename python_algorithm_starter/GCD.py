# 유클리드 호제법 최대공약수 구하기

N = int(input())
A = list(map(int, input().split()))
A.sort()
i = 0
Max = 0
b = A[i+1] % A[i]

for i in range(N):
    if A[i] % b == 0:
        if i != N -1:
            continue
        Max = b
        break
    else:
        b = A[i] % b
print(Max)