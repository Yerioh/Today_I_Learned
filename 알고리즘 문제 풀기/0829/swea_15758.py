import sys

sys.stdin = open("txt/in_15758.txt", "r")

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    S, T = input().split()  # 두 문자열 S, T
    s, t = len(S), len(T)
    # 두 문자열의 길이를 같게 하여 비교
    answer = "yes" if S * t == T * s else "no"
    print(f"#{tc} {answer}")
