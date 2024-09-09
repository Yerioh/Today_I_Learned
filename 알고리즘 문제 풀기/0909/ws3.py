import sys

sys.stdin = open("txt/in_ws3.txt", "r")


def get_max_break(lev, remains, blocks):  # 현재 진행 횟수, 남은 블록 수, 현재 블록 배치
    global result
    if lev == N or remains == 0:
        result = min(result, remains)
        return
    for col in range(W):
        arr = [rows[:] for rows in blocks]
        for row in range(H):
            if arr[row][col]:
                # 블록 부수기
                stack = [(row, col, arr[row][col])]
                cnt = 1  # 깬 블록 수
                arr[row][col] = 0
                while stack:
                    vr, vc, power = stack.pop()
                    # 상하좌우를 블록 번호만큼 순회
                    for i in range(1, power):
                        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nr, nc = vr + dr * i, vc + dc * i
                            if 0 <= nr < H and 0 <= nc < W and arr[nr][nc]:
                                stack.append((nr, nc, arr[nr][nc]))
                                arr[nr][nc] = 0
                                cnt += 1
                # 블록 재배치
                for c in range(W):
                    idx = H - 1
                    for r in range(H - 1, -1, -1):
                        if arr[r][c]:
                            arr[r][c], arr[idx][c] = arr[idx][c], arr[r][c]
                            idx -= 1
                get_max_break(lev + 1, remains - cnt, arr)
                break


T = int(input())  # 테스트 케이스의 수
answer = [""] * T
for tc in range(T):
    N, W, H = map(int, input().split())  # 구슬을 떨어트릴 횟수, 벽돌 배열의 크기
    bricks = [list(map(int, input().split())) for _ in range(H)]  # W*H 크기의 벽돌 배열
    result = 1e9  # 남은 블록이 제일 적을 때 가장 많이 깬 것
    # 최초 블록 수
    brick_cnt = 0
    for items in bricks:
        for item in items:
            if item:
                brick_cnt += 1
    get_max_break(0, brick_cnt, bricks)
    answer[tc] = f"#{tc + 1} {result}"
print(*answer, sep="\n")
