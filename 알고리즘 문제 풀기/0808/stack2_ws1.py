import sys

sys.stdin = open('txt/input_ws1.txt', 'r')


def is_valid(r, c, n):
    return 0 <= r < n and 0 <= c < n


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N = int(input())  # 미로의 크기 N
    maze = [list(map(int, input())) for _ in range(N)]
    sr, sc = 0, 0  # 시작점 초기화
    for i in range(N):  # 시작점의 열 찾기
        for j in range(N):
            if maze[i][j] == 2:
                sr, sc = i, j
    # 이동 가능한 구간 찾기
    #     상        하       좌       우
    dl = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[0] * N for _ in range(N)]  # 방문 확인
    stack = []  # 스택 초기화
    visited[sr][sc] = 1  # 시작점은 방문
    vr, vc = sr, sc  # 시작점 설정
    answer = 0  # 정답 초기화
    while True:
        if maze[vr][vc] == 3:
            answer = 1
            break
        # 델타 배열을 순회하여 움직일 수 있는 곳 찾기
        for dr, dc in dl:
            nr, nc = vr + dr, vc + dc
            # 인덱스 범위 확인, 방문 확인, 통로인지 확인
            if is_valid(nr, nc, N) and not visited[nr][nc] and maze[nr][nc] != 1:
                stack.append((vr, vc))
                visited[nr][nc] = 1
                vr, vc = nr, nc
                break
        else:  # break 되지 않았다면
            if stack:  # 되돌아갈 곳이 있다면
                vr, vc = stack.pop()
            else:
                break
    print(f'#{tc} {answer}')
