import sys

sys.stdin = open("txt/in_pr6.txt", "r")

T = int(input())
for t in range(1, T + 1):
    N, X = map(int, input().split())  # 지도의 크기 N, 경사로의 길이 X
    arr = [list(map(int, input().split())) for _ in range(N)]  # 지형 정보 배열
    answer = 0
    for _ in range(2):
        for i in range(N):
            row_height = arr[i][0]  # 첫 지형 높이
            row_check = 1  # 경사로 가능 여부
            row_len = 0  # 같은 높이의 길이
            row_cnt = 0  # 현재 필요한 경사로 수
            for j in range(N):
                if arr[i][j] == row_height:
                    row_len += 1
                elif arr[i][j] < row_height:
                    row_cnt += 1
                    row_len = 1
                elif arr[i][j] > row_height:
                    if row_len < X:
                        row_check = 0
                    row_len = 1
                row_height = arr[i][j]
                if row_cnt > 0 and row_len == X:
                    row_cnt -= 1
                    row_len -= X
            if row_cnt <= 0 and row_check:
                answer += 1
        # 행 열 뒤집기
        arr = list(map(list, zip(*arr)))
    print(f"#{t} {answer}")
