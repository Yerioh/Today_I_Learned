import sys

sys.stdin = open("txt/in_13732.txt", "r")

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N = int(input())  # 격자판의 크기
    arr = [input() for _ in range(N)]  # 격자판의 모양
    # 처음으로 막힌 곳 찾기
    sr = sc = -1
    for r in range(N):
        for c in range(N):
            if arr[r][c] == "#":
                sr, sc = r, c
                break
        if sr >= 0:
            break
    # 마지막으로 막힌 곳 찾기
    er = ec = N
    for r in range(N - 1, -1, -1):
        for c in range(N - 1, -1, -1):
            if arr[r][c] == "#":
                er, ec = r, c
                break
        if er < N:
            break
    answer = "yes"
    # 정사각형이 아니라면
    if sr - er != sc - ec:
        answer = "no"
    # 중간에 .이 들어있는지 확인
    for r in range(sr, er + 1):
        for c in range(sc, ec + 1):
            if arr[r][c] == ".":
                answer = "no"
    print(f"#{tc} {answer}")
