N = int(input())
B = list(map(int, input().split()))
R = list(map(int, input().split()))
sum = 0
result = 0

for i in B:
    sum += i
    if i == B[-1]:
        result = sum // N

sum = 0
for j in R:
    sum += j
    if j == R[-1]:
        result = result + sum // N
print(result)
