import sys

sys.stdin = open("txt/in04.txt", "r")

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 사진의 크기
    arr = [list(map(int, input().split())) for _ in range(N)]  # 사진 데이터
    answer = 0  # 구조물이 없는 경우라면 0을 출력
    for r in range(N):
        for c in range(M):
            if arr[r][c]:
                row_cnt = 1
                for i in range(c + 1, M):  # 행 탐색
                    if not arr[r][i]:
                        break
                    row_cnt += 1
                if row_cnt > 1 and row_cnt > answer:  # 길이가 2이상인 경우에만 구조물
                    answer = row_cnt
                col_cnt = 1
                for j in range(r + 1, N):  # 열 탐색
                    if not arr[j][c]:
                        break
                    col_cnt += 1
                if col_cnt > 1 and col_cnt > answer:
                    answer = col_cnt
    print(f"#{tc} {answer}")
