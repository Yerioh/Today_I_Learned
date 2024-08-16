T = int(input())
for tc in range(1, T + 1):
    N, D = map(int, input().split())  # 정원의 크기 N, 분무기의 범위 D
    answer = N // (D * 2 + 1) + 1 if N % (D * 2 + 1) else N // (D * 2 + 1)  # 분무기의 개수
    print(f"#{tc} {answer}")
