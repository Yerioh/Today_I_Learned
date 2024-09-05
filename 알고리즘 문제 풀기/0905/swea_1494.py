import sys

sys.stdin = open("txt/in_1494.txt", "r")


def get_perm(lev, perm, x, y, selected):
    if x * x + y * y > max_vector:
        return
    if lev == N:
        print(perm)
        return
    for i in range(N):
        selected[i] = 1
        perm[lev] = i
        if not selected[i]:
            for j in range(N):
                if not selected[j]:
                    selected[j] = 1
                    perm[lev + 1] = j
                    temp_x, temp_y = arr[j][0] - arr[i][0], arr[j][1] - arr[i][1]
                    get_perm(lev + 2, perm, temp_x + x, temp_y + y, selected)
                    selected[j] = 0
        selected[i] = 0


T = int(input())
answer = [""] * T
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    max_vector = (2000000 ** 2) * 2
    get_perm(0, [0] * N, 0, 0, [0] * N)
    answer[tc - 1] = f"#{tc} "
print(*answer, sep="\n")
