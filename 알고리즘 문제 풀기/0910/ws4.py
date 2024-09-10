import sys

sys.stdin = open("txt/in_ws4.txt", "r")

from collections import deque

# 상, 우상, 우, 우하, 하, 좌하, 좌, 좌상
dl = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def click_item(r, c):
    q = deque()
    q.append((r, c))
    while q:
        vr, vc = q.popleft()
        cnt = 0  # 지뢰의 개수
        temp = deque()
        for d in range(8):
            nr, nc = vr + dl[d][0], vc + dl[d][1]
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == "*":  # 지뢰라면
                    cnt += 1
                elif arr[nr][nc] == ".":  # 아직 모르는 칸이라면
                    temp.append((nr, nc))
        arr[vr][vc] = cnt  # 해당 칸은 주변 지뢰수로 변경
        if not cnt:  # 지뢰가 없다면
            while temp:  # 임시 큐에 있는 것을 큐로 옮기기
                q.append(temp.popleft())


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N = int(input())  # 지뢰 찾기 게임의 크기
    arr = [list(input()) for _ in range(N)]  # 지뢰 위치 표시
    answer = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == ".":
                click_item(i, j)
                answer += 1
    print(f"#{tc} {answer}")
