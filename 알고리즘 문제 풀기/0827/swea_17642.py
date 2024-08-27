import sys

sys.stdin = open("txt/in_17642.txt", "r")

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    A, B = map(int, input().split())  # 두 정수 A, B
    answer = -1
    # 두 수의 차가 1이 아닐 경우에만 두 수를 같게 할 수 있다
    # 최대한 많이 시행하려면 2, 3 만을 더하거나 뺀다
    # 두 수의 차가 1이 된다면 앞 시행에서 3을 더한 것으로 간주
    # 두 수의 차를 2로 나눈 나머지가 가장 많은 시행 횟수
    if (B - A) > 1:
        answer = (B - A) // 2
    elif B - A == 0:
        answer = 0
    print(f"#{tc} {answer}")
