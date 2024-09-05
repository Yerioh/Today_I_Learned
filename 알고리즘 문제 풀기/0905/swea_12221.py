T = int(input())
for tc in range(1, T + 1):
    A, B = map(lambda x: -1 if len(x) >= 2 else int(x), input().split())
    print(f"#{tc} {A * B if A != -1 and B != -1 else -1}")




