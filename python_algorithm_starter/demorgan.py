# 1부터 12까지 8을 건너뛰고 출력하기 1
for i in range(1, 13):
    if i == 8:
        continue
    print(i, end=' ')

print()

# 이는 if문 판단을 많이 하기 때문에 매우 비효율적

# 아래는 조금 효율적이게 작성한 코드
# 1부터 12까지 8을 건너뛰고 출력하기 2
for i in list(range(1, 8)) + list(range(9, 13)):
    print(i, end=' ')

print()

# 위의 코드 2는 1보단 효율적이지만 생성한 리스트의 원소를 하나씩 꺼내 반복하므로 반복을 위한 연산 비용이 여전히 발생.

# 2자리 양수(10~99) 입력받기
# 비교연산자를 연속으로 사용 하는 방법
print('2자리 양수를 입력하세요.')

while True:
    no = int(input('값을 입력하세요.: '))
    if no >= 10 and no <= 99:
        break;
print(f'입력받은 양수는 {no} 입니다.')

# 드모르간의 법칙을 사용한 방법
while True:
    no = int(input('값을 입력하세요.: '))
    if not(no < 10 or no > 99):
        break;
print(f'입력받은 양수는 {no} 입니다.')

