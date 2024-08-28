import sys

sys.stdin = open("txt/in_16800.txt", "r")

T = int(input())  # 테스트케이스의 수
for tc in range(1, T + 1):
    N = int(input())  # 찾아야할 정수 N
    # N의 제곱근 범위까지만 확인
    num = 0
    for i in range(1, int(N ** 0.5) + 1):
        if not N % i:
            num = i
    print(f"#{tc} {num + N // num - 2}")
