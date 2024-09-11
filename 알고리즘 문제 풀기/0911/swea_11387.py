import sys

sys.stdin = open("txt/in_11387.txt", "r")

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    D, L, N = map(int, input().split())
    answer = 0
    for i in range(N):
        answer += D // 100 * (100 + i * L)
    print(f"#{tc} {answer}")
