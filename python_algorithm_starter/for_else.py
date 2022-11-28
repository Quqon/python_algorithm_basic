# 10 ~ 99 사이의 난수 n개 생성하기(13 나오면 중단)

import random

n = int(input('난수의 개수를 입력하세요.: '))

for _ in range(n):
    r = random.randint(10, 99)                        # random의 randint메소드는 인자로 오는 두 수 사이의 숫자를 랜덤으로 반환 함.
    print(r, end=' ')
    if r == 13:
        print('\n프로그램을 중단합니다.')
        break
else:
    print('\n난수 생성을 종료합니다.')                   # for문 종료 후 else문 실행, 그 후 프로그램 종료.