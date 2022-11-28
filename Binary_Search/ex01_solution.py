n = int(input())
requests = list(map(int, input().split()))               #map함수를 써서 input으로 들어오는 입력값을 int형으로 만들고 list메소드로 list로 만들어 할당함.
budget = int(input())

def calculate_needed_budget(upper_bound: int) -> int:
    # 상한액이 upper_bound 일 때 필요한 예산을 계산하는 함수.

    needed_budget = 0
    for request in requests:
        needed_budget += min(request, upper_bound)

    return needed_budget

# 이분 탐색을 수행하는 메인 로직
low = 0
high = max(requests)
good_upper_bound = -1

while low <= high:
    mid = (low + high) // 2

    if calculate_needed_budget(mid) <= budget:
        good_upper_bound = mid
        low = mid + 1
    else:
        high = mid - 1