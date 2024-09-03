import sys

sys.stdin = open("txt/in_13547.txt", "r")

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    S = input()
    answer = "YES" if S.count("x") <= 7 else "NO"
    print(f"#{tc} {answer}")
