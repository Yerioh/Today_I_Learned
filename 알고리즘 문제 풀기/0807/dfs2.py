# miro[i][j] == 0 : 이동 가능한 칸
# miro[i][j] == 1 : 이동 불가능한 벽
# miro[i][j] == 3 : 도착점
miro = [
    [0, 0, 0, 0, 1, 3],
    [1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0]
]

dr = [-1, 1, 0, 0]  # 행번호 변화량
dc = [0, 0, -1, 1]  # 열번호 변화량

n = 6


def is_vaild(r, c):
    return 0 <= r < n and 0 <= c < n


# dfs 로 2차원 배열 순회하기 (미로찾기)
def dfs(r, c, n):
    # 방문 배열
    visited = [[0] * n for _ in range(n)]
    # 스택
    stack = []
    # 시작 체크
    visited[r][c] = 1

    while True:
        if miro[r][c] == 3:
            print('도착')
            return
        # 현재 위치(r, c)에서 방문 가능한 곳 탐색
        # 상하좌우로 움직일 수 있나 확인, 움직일 수 있으면 가자
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if is_vaild(nr, nc) and not visited[nr][nc] and miro[nr][nc] != 1:
                stack.append((r, c))
                visited[r][c] = 1
                r, c = nr, nc
                break
        else:
            if stack:
                r, c = stack.pop()
            else:
                break


dfs(0, 0, n)
