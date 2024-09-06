import sys

sys.stdin = open("txt/in_ws3.txt", "r")

# 정사각형 방


def get_max_path(r, c, start, path):  # 현재 위치, 시작 방번호, 이동한 방 횟수
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 상하좌우 탐색
        nr, nc = r + dr, c + dc
        # 인덱스 검사, 다음 방이 1보다 큰지 검사
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] - arr[r][c] == 1:
            get_max_path(nr, nc, start, path + 1)
            break
    else:  # 다음 위치를 탐색하지 못했다면
        global max_path
        global answer
        if path > max_path:
            max_path = path
            answer = start
        elif path == max_path and start < answer:
            answer = start
        return


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N = int(input())  # 방 배열의 크기
    arr = [list(map(int, input().split())) for _ in range(N)]  # 각 방의 번호
    max_path = 0  # 가장 많이 이동한 방 수
    answer = N ** 2 + 1  # 가장 많이 이동한 경우의 첫 위치
    for i in range(N):
        for j in range(N):
            r, c = i, j
            start = arr[i][j]
            path = 1
            while True:
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 상하좌우 탐색
                    nr, nc = r + dr, c + dc
                    # 인덱스 검사, 다음 방이 1보다 큰지 검사
                    if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] - arr[r][c] == 1:
                        r, c = nr, nc
                        path += 1
                        break
                else:  # 다음 위치를 탐색하지 못했다면
                    if path > max_path:
                        max_path = path
                        answer = start
                    elif path == max_path and start < answer:
                        answer = start
                    break
    print(f"#{tc} {answer} {max_path}")
