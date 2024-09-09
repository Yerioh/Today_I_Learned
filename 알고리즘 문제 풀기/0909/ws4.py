import sys

sys.stdin = open("txt/in_ws4.txt", "r")


def get_max_min(lev, num):
    global max_num, min_num
    if lev == N:  # 계산이 끝났다면
        max_num = max(max_num, num)
        min_num = min(min_num, num)
        return
    operators = "+-*/"
    for i in range(4):
        if operator_selected[i]:  # 연산자가 남아있다면
            operator_selected[i] -= 1
            temp = num  # 계산 결과를 담을 임시 변수
            # 연산자에 따라 계산
            if operators[i] == "+":
                temp += numbers[lev]
            elif operators[i] == "-":
                temp -= numbers[lev]
            elif operators[i] == "*":
                temp *= numbers[lev]
            elif operators[i] == "/":
                if temp < 0:  # 이전 결과가 음수라면
                    temp = -(abs(temp) // numbers[lev])
                else:
                    temp //= numbers[lev]
            get_max_min(lev + 1, temp)
            operator_selected[i] += 1


T = int(input())  # 테스트 케이스의 수
answer = [""] * T
for tc in range(T):
    N = int(input())  # 정수의 개수
    operator_selected = list(map(int, input().split()))  # 각 연산자 카드의 개수
    numbers = list(map(int, input().split()))  # N개의 정수들
    max_num = -100000000
    min_num = 100000000
    get_max_min(1, numbers[0])  # 첫 숫자
    result = max_num - min_num
    answer[tc] = f"#{tc + 1} {result}"
print(*answer, sep="\n")
