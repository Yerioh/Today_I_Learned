T = int(input())
for tc in range(1, T + 1):
    A, B, C = map(int, input().split())
    answer = 0
    if C <= B:
        eat = B - C + 1
        answer += eat
        B -= eat
    if B <= A:
        eat = A - B + 1
        answer += eat
        A -= eat
    if A <= 0 or B <= 0:
        answer = -1
    print(f"#{tc} {answer}")
