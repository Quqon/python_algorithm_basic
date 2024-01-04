N, S = map(int, input().split())
Maximum = max(N, S)
Minimum = min(N, S)
a = Maximum % Minimum
b = 0

while True:
    if a != 0:
        b = a
        a = Minimum % a
        Minimum = b
    else:
        break
print(Minimum)