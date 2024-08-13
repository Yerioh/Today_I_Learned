import sys

sys.stdin = open('txt/in03.txt', 'r')

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 구역의 크기 N, M
    arr = [list(map(int, input().split())) for _ in range(N)]  # 각 지역의 높이
    answer = 0  # 예비 후보지의 개수
    # 확인하는 지점의 주변 방향
    # 좌상 상 우상 좌 우 좌하 하 우하
    dl = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for i in range(N):
        for j in range(M):
            cnt = 0  # 착륙지보다 낮은 지역의 수
            height = arr[i][j]  # 착륙지의 높이
            for dr, dc in dl:
                r, c = i + dr, j + dc
                # 인덱스 범위 확인, 높이가 낮은지 확인
                if 0 <= r < N and 0 <= c < M and arr[r][c] < height:
                    cnt += 1
            # 낮은 지역의 수가 4이상이면 예비 후보지
            if cnt >= 4:
                answer += 1
    print(f'#{tc} {answer}')
