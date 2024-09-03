import sys

sys.stdin = open("txt/in_14718.txt", "r")

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N, D = map(int, input().split())  # 꽃밭의 길이, 분무기의 범위
    D = D * 2 + 1
    print(f"#{tc} {N // D + (1 if N % D else 0)}")
