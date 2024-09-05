"""
3
100 1 50
1000 81 83
10 10 100

"""

T = int(input())
for tc in range(1, T + 1):
    N, D, G = map(int, input().split())
    answer = "Possible"
    if (G == 100 and D != 100) or (G == 0 and D != 0):
        answer = "Broken"
    else:
        for i in range(1, N + 1):
            if i * D / 100 == i * D // 100:
                break
        else:
            answer = "Broken"
    print(f"#{tc} {answer}")
