import sys

sys.stdin = open("txt/in_3234.txt", "r")


def fac(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def libra(lev, left, right, selected):
    global cnt
    if left < right:
        return
    if sum_w - left < left:
        n = N - lev
        cnt += (2 ** n) * fac(n)
        return
    if lev == N:
        cnt += 1
        return
    for i in range(N):
        if not selected[i]:
            selected[i] = 1
            libra(lev + 1, left + arr[i], right, selected)
            libra(lev + 1, left, right + arr[i], selected)
            selected[i] = 0


T = int(input())
answer = [""] * T
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    sum_w = sum(arr)
    cnt = 0
    libra(0, 0, 0, [0] * N)
    print(f"#{tc} {cnt}")
