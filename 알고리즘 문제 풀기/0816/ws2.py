import sys

sys.stdin = open("txt/in_ws2.txt", "r")

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 풍선 배열의 크기
    arr = [list(map(int, input().split())) for _ in range(N)]  # 각 풍선의 꽃가루 배열
    dl = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 주변 풍선을 알기위한 방향 배열
    answer = 0  # 가장 많은 꽃가루 수
    for r in range(N):
        for c in range(M):
            s = arr[r][c]
            # 기준 풍선의 꽃가루 수만큼 확인
            for i in range(1, arr[r][c] + 1):
                for dr, dc in dl:
                    nr, nc = r + dr * i, c + dc * i
                    if 0 <= nr < N and 0 <= nc < M:  # 인덱스 범위 확인
                        s += arr[nr][nc]
            if s > answer:  # 현재 합이 기존 최댓값보다 크다면
                answer = s
    print(f"#{tc} {answer}")
