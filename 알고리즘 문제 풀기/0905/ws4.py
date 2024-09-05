import sys

sys.stdin = open("txt/in_ws4.txt", "r")


def get_max_percent(emp, percent, selected):
    global answer
    if percent <= answer:  # 이미 작으면 가지치기
        return
    if emp == N:
        answer = percent
        return
    for work in range(N):  # 순열을 만들어 확률 구하기
        if not selected[work]:
            selected[work] = 1
            temp = arr[emp][work] * 0.01
            get_max_percent(emp + 1, percent * temp, selected)
            selected[work] = 0


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N = int(input())  # 직원 및 업무의 수
    arr = [list(map(int, input().split())) for _ in range(N)]  # 해당 직원이 각 일을 성공할 확률
    answer = 0
    get_max_percent(0, 100, [0] * N)
    print(f"#{tc} {answer:.6f}")
