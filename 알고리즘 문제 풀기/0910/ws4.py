import sys

sys.stdin = open("txt/in_ws4.txt", "r")

from collections import deque

# 상, 우상, 우, 우하, 하, 좌하, 좌, 좌상
dl = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def chain_zero(r, c):  # 해당 칸을 눌러 연쇄된 곳을 찾기
    q = deque()
    q.append((r, c))
    arr[r][c] = "."  # 추가로 세지 않기 위해 표기 변경
    while q:
        vr, vc = q.popleft()
        # 0주변은 다 연쇄로 반응했으므로 전부 표기 변경
        for dr, dc in dl: 
            nr, nc = vr + dr, vc + dc
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == "0":  # 0이라면 해당 칸 주변으로 또 연쇄하기 위해 큐에 넣음
                    arr[nr][nc] = "."
                    q.append((nr, nc))
                elif arr[nr][nc] != "*":  # 0이 아니고 지뢰가 아니면
                    arr[nr][nc] = "."

def get_mine_cnt(r, c):  # 주변 지뢰수 계산
    cnt = 0
    for dr, dc in dl:
            nr, nc = r + dr, c + dc
            # 인덱스 확인, 지뢰 수 계산
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == "*": 
                cnt += 1
    return str(cnt)


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N = int(input())  # 지뢰 찾기 게임의 크기
    arr = [list(input()) for _ in range(N)]  # 지뢰 위치 표시
    # . 을 정답에 맞는 숫자로 변경
    for i in range(N):
        for j in range(N):
            if arr[i][j] == ".":
                arr[i][j] = get_mine_cnt(i, j)
    # 연쇄된 부분 찾기
    # 0인 경우에만 연쇄가 일어남
    # 연쇄가 일어나는 부분의 어떤 0을 눌러도 같은 결과가 나옴
    answer = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == "0":
                answer += 1
                chain_zero(i, j)
    # 연쇄 후에 남은 숫자들은 연쇄하지 않는 칸이므로 다 하나씩 클릭
    for i in range(N):
        for j in range(N):
            if arr[i][j] not in "*.": 
                answer += 1
    print(f"#{tc} {answer}")