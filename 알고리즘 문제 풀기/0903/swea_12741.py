T = int(input())
answer_list = [""] * T
for tc in range(1, T + 1):
    A, B, C, D = map(int, input().split())
    answer = 0
    start = A if A >= C else C
    end = B if B <= D else D
    answer = end - start
    answer = answer if answer > 0 else 0
    answer_list[tc - 1] = f"#{tc} {answer}"
print(*answer_list, sep="\n")
