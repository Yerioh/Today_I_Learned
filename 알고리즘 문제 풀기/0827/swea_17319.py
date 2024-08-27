import sys

sys.stdin = open("txt/in_17319.txt", "r")

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N = int(input())  # 문자열의 길이
    s = input()  # 입력받은 문자열
    answer = "No"
    if N % 2 == 0 and s[:N // 2] == s[N // 2:]:
        answer = "Yes"
    print(f"#{tc} {answer}")
