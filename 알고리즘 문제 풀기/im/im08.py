import sys

sys.stdin = open("txt/in08.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 깃발의 크기 N, M
    arr = [list(input()) for _ in range(N)]  # 2차원 배열 형태의 깃발
    answer = N * M  # 가장 적게 칠할 때의 칸 수(모든 칸을 칠해야 할 경우가 최댓값)
    # w, b, r의 비중 배열
    color_rate = []
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            for k in range(1, N - 1):
                if i + j + k == N:
                    color_rate.append((i, j, k))
    for white, blue, red in color_rate:
        cnt = 0  # 칠한 횟수
        row = 0  # 위에서 부터 칠하기 위해 현재 행 위치
        for _ in range(white):  # 흰색 칠하기
            for c in range(M):
                if arr[row][c] != "W":
                    cnt += 1
            row += 1
        for _ in range(blue):  # 파란색 칠하기
            for c in range(M):
                if arr[row][c] != "B":
                    cnt += 1
            row += 1
        for _ in range(red):  # 빨간색 칠하기
            for c in range(M):
                if arr[row][c] != "R":
                    cnt += 1
            row += 1
        if cnt < answer:  # 최솟값 교체
            answer = cnt
    print(f"#{tc} {answer}")
