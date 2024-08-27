import sys

sys.stdin = open("txt/in_16910.txt", "r")

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N = int(input())  # 반지름의 길이
    X = [i for i in range(N * (-1), N + 1)]
    Y = [i for i in range(N * (-1), N + 1)]
    answer = 0
    for x in X:
        for y in Y:
            if x ** 2 + y ** 2 <= N ** 2:
                answer += 1
    print(f"#{tc} {answer}")
