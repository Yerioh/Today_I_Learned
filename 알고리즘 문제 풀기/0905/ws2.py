import sys

sys.stdin = open("txt/in_ws2.txt", "r")


def get_min_cost(prd, cost, selected):
    global answer
    if cost >= answer:  # 현재 정답이상이라면
        return
    if prd == N:  # 제품별 공장이 모두 선택되었다면
        answer = cost
        return
    for fac in range(N):
        if not selected[fac]:  # 선택되지 않은 공장이라면
            selected[fac] = 1
            get_min_cost(prd + 1, cost + arr[prd][fac], selected)
            selected[fac] = 0


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N = int(input())  # 제품 및 공장의 수
    arr = [list(map(int, input().split())) for _ in range(N)]  # 공장별 각 제품 생산 비용
    answer = 100 * N
    get_min_cost(0, 0, [0] * N)
    print(f"#{tc} {answer}")
