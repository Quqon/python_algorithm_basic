# 내가 작성한 풀이
# area = int(input('직사각형의 넓이를 입력하세요: '))
#
# li = []
#
# for i in range(1, area + 1):
#     if area % i == 0:
#         mock = area // i
#
#         if not li.index(mock):                    # ValueError가 발생한다. 예외처리를 해주면 가능할 것 같지만 알고리즘에서 예외처리를 이용하는지 모르겠다.
#             li.append(mock)
#             continue
#         else:
#             print('end')
#             break
#     print(f'{i} X {mock}')

#문제집 풀이
area = int(input('직사각형의 넓이를 입력하세요: '))

for i in range(1, area + 1):
    if i * i > area: break                        # 짧은 변과 긴 변의 길이를 구별하지 않음.
    if area % i: continue                         # 32의 약수가 아닌 수는 제외.
    print(f'{i} x {area // i}')