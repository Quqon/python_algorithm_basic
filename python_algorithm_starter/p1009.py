import sys
T = int(input(""))

for i in range(0, T):
    a, b = map(int, sys.stdin.readline().split())
    c = pow(a, b, 10)
    if c == 0:
        print(10)
    else:
        print(c)