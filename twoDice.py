redDice = [10, 20, 30, 40, 50, 60]
blueDice = [0, 1, 3, 5, 6, 9]
expectedResult = 0
sum = 0

for i in redDice:
    sum += i

for j in blueDice:
    sum += j

expectedResult = sum // 6
print(expectedResult)