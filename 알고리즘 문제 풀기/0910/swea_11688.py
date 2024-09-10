import sys

sys.stdin = open("txt/in_11688.txt", "r")

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    path = input()
    a = 1
    b = 1
    for p in path:  # path를 따라 a와 b의 값을 변경
        if p == "L":
            b = a + b
        elif p == "R":
            a = a + b
    print(f"#{tc} {a} {b}")
