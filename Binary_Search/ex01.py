# 문제
# 국가의 역할 중 하나는 여러 지방의 예산요청을 심사하여 국가의 예산을 분배하는 것이다. 국가예산의 총액은 미리 정해져 있어서 모든 예산요청을 배정해 주기는 어려울 수도 있다. 그래서 정해진 총액 이하에서 가능한 한 최대의 총 예산을 다음과 같은 방법으로 배정한다.

# 모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정한다.
# 모든 요청이 배정될 수 없는 경우에는 특정한 정수 상한액을 계산하여 그 이상인 예산요청에는 모두 상한액을 배정한다. 상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정한다. 
# 예를 들어, 전체 국가예산이 485이고 4개 지방의 예산요청이 각각 120, 110, 140, 150이라고 하자. 이 경우, 상한액을 127로 잡으면, 위의 요청들에 대해서 각각 120, 110, 127, 127을 배정하고 그 합이 484로 가능한 최대가 된다. 

# 여러 지방의 예산요청과 국가예산의 총액이 주어졌을 때, 위의 조건을 모두 만족하도록 예산을 배정하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에는 지방의 수를 의미하는 정수 N이 주어진다. N은 3 이상 10,000 이하이다. 다음 줄에는 각 지방의 예산요청을 표현하는 N개의 정수가 빈칸을 사이에 두고 주어진다. 이 값들은 모두 1 이상 100,000 이하이다. 그 다음 줄에는 총 예산을 나타내는 정수 M이 주어진다. M은 N 이상 1,000,000,000 이하이다. 

# 출력
# 첫째 줄에는 배정된 예산들 중 최댓값인 정수를 출력한다. 

budget = [120, 130, 140, 40, 100]
N = 5
total = 450

def solution1(N, budget, total):
    sum = 0
    num = 0
    sortSum = 0
    # 숫자 배열에서 두번째 큰값 찾기
    # second = largest = -float('inf')
    # for n in range(budget):
    #     if n > largest:
    #         second = largest
    #         largest = n
    #     elif second < n < largest:
    #         second = n
    # print(second)
    
    # 숫자 배열에서 메소드를 이용해 두번째 큰값 찾기
    sortNum = sorted(set(budget), reverse = True)
    second = sortNum[1]

    for i in range(len(budget)):
        sum += budget[i]
    if sum > total:
        num = (sum - total + 1) / (len(budget) - 1)

        newNum1 = max(budget) - (num * (len(budget) - 2))

        newNum2 = second - num

        for i in range(2, len(sortNum)):
            sortSum += sortNum[i]

        result = newNum1 + newNum2 + sortSum
        print(result)

        print(newNum1, newNum2)

        # 총 합은 총 예산 보다 작을 수 있는 최댓값으로 잘 나오지만, 가장 많이 지급할 수 있는 예산의 값이 원하는 대로 나오지 않는다.


solution1(N, budget, total)

# 이분탐색방법 듣고 풀이
def solution2(N, budget, total):
    largest = max(budget)
    sum = 0

    def get_limit(value):
        limit = (value + largest) / 2
        return limit

    # 상한 액은 0 ~ largest
    for i in range(len(budget)):
        sum += budget[i]
        if get_limit(0) < budget[i]:
            sum += get_limit(0)
    
    result = largest - sum
    
    while True:
        if result == False:
            return get_limit(0)
        elif result > 0:
            limit = get_limit(0)
            sum = 0
            for i in range(len(budget)):
                sum += budget[i]
                if get_limit(limit) < budget[i]:
                    sum += get_limit(limit)
        elif result < 0:
            break

        # 계속 반복되어 풀리지 않는다.