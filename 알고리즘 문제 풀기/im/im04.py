import sys

sys.stdin = open('txt/in04.txt', 'r')

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 배열의 크기 N, M
    arr = [list(map(int, input().split())) for _ in range(N)]  # 사진 속 구조물의 배치
    answer = 0  # 가장 긴 구조물의 길이
    for i in range(N):
        for j in range(M):
            if arr[i][j]:  # 해당 포인트에 구조물의 부분이 보일 때
                # 가로 검사
                c = j
                row_cnt = 0
                while c < M and arr[i][c] != 0:  # 인덱스 범위 내이며 해당 위치가 1이라면
                    row_cnt += 1
                    c += 1
                if row_cnt > answer:
                    answer = row_cnt
                # 세로 검사
                r = i
                col_cnt = 0
                while r < N and arr[r][j] != 0:  # 인덱스 범위 내이며 해당 위치가 1이라면
                    col_cnt += 1
                    r += 1
                if col_cnt > answer:
                    answer = col_cnt
    print(f'#{tc} {answer}')
