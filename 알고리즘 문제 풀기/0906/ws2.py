import sys

sys.stdin = open("txt/in_ws2.txt", "r")

# 수영장


def get_min_price(lev, result):  # 현재 위치, 월 이용요금 계산
    global answer
    if result >= answer:
        return
    if lev == 12:
        answer = result
        return
    day_price = d * arr[lev]  # 일일 이용권 이용금액
    get_min_price(lev + 1, result + day_price)  # 일일 이용권으로 결제시
    get_min_price(lev + 1, result + m1)  # 1개월 이용권 결제시
    if lev < 10:
        get_min_price(lev + 3, result + m3)  # 3개월 이용권 결제시


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    # 일일, 1개월, 3개월, 1년
    d, m1, m3, y = map(int, input().split())
    arr = list(map(int, input().split()))  # 월별 이용 계획
    answer = y
    get_min_price(0, 0)
    print(f"#{tc} {answer}")
