import sys

sys.stdin = open('txt/in01.txt', 'r')

# 파리퇴치 3
T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 배열의 크기 N, 노즐의 파워 M
    arr = [list(map(int, input().split())) for _ in range(N)]  # 파리의 수 배열
    # 상하좌우 델타 배열
    dl1 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # 좌상좌하우상우하 델타 배열
    dl2 = [(-1, -1), (1, -1), (-1, 1), (1, 1)]
    answer = 0  # 정답 초기화
    for r in range(N):
        for c in range(N):
            s1 = arr[r][c]  # 상하좌우 합
            s2 = arr[r][c]  # 대각선 합
            # 노즐의 파워 - 1 만큼 반복(본인 제외했기 때문)
            for i in range(1, M):
                # 상하좌우 계산
                for dr, dc in dl1:
                    # 계산해야 하는 위치
                    vr, vc = r + dr * i, c + dc * i
                    if 0 <= vr < N and 0 <= vc < N:  # 인덱스 범위 안이라면
                        s1 += arr[vr][vc]
                # 대각선 계산
                for dr, dc in dl2:
                    vr, vc = r + dr * i, c + dc * i
                    if 0 <= vr < N and 0 <= vc < N:  # 인덱스 범위 안이라면
                        s2 += arr[vr][vc]
            s = s1 if s1 >= s2 else s2  # 둘 중 큰 값
            if s > answer:  # 최댓값 갱신
                answer = s
    print(f'#{tc} {answer}')
