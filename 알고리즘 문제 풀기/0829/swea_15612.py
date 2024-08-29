import sys

sys.stdin = open("txt/in_15612.txt", "r")


def check_rook(vr, vc):
    # 배열을 순회하면서 위와 왼쪽은 체크되었으므로
    # 오른쪽과 아래만 체크
    dl = [(0, 1), (1, 0)]
    for dr, dc in dl:
        nr, nc = vr + dr, vc + dc
        while nr < 8 and nc < 8:
            if arr[nr][nc] == "O":
                return False
            # 검증 후 다음 값으로 이동
            nr += dr
            nc += dc
    return True


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    # 8*8 크기의 체스판
    arr = [list(input()) for _ in range(8)]
    answer = "yes"
    cnt = 0
    for i in range(8):
        for j in range(8):
            if arr[i][j] == "O":
                cnt += 1
            if arr[i][j] == "O" and not check_rook(i, j):  # 검증을 실패했다면
                answer = "no"
    if cnt != 8:
        answer = "no"
    print(f"#{tc} {answer}")
