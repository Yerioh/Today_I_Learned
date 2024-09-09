import sys

sys.stdin = open("txt/in_test1.txt", "r")

dl = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우 델타 배열
# 각 터널이 연결될 수 있는 모양 확인
linked = [[], ["1256", "1247", "1345", "1367"], ["1256", "1247", "", ""],
          ["", "", "1345", "1367"], ["1256", "", "", "1367"],
          ["", "1247", "", "1367"], ["", "1247", "1345", ""],
          ["1256", "", "1345", ""]]  # [상, 하, 좌, 우]


def is_valid(r, c):
    if 0 <= r < N and 0 <= c < M:
        return True
    return False


def check_pb(lev, r, c):  # 현재 경과된 시간, 현재 위치
    if lev == L:  # 시간이 부족하여 더 이상 진행 불가
        return
    t = int(arr[r][c])  # 현재 터널의 모양
    # 다음 위치 확인
    for d in range(4):  # 상하좌우
        nr, nc = r + dl[d][0], c + dl[d][1]
        # 인덱스 확인, 체크한 곳인지 또는 더 빠르게 올 수 있는 곳인지, 연결되어있는지 확인
        if is_valid(nr, nc) and (not checked[nr][nc] or checked[nr][nc] > lev) and arr[nr][nc] in linked[t][d]:
            checked[nr][nc] = lev  # 위치를 체크
            check_pb(lev + 1, nr, nc)


T = int(input())  # 테스트 케이스의 수
answer = [""] * T
for tc in range(T):
    N, M, R, C, L = map(int, input().split())  # 지하터널의 크기, 맨홀 위치, 탈출 후 소요 시간
    arr = [input().split() for _ in range(N)]  # 지하터널의 모양
    checked = [[0] * M for _ in range(N)]  # 각 위치를 확인했는지 여부
    # 숨어있을 수 있는 곳 체크
    checked[R][C] = 1
    check_pb(1, R, C)
    # 체크된 곳 세기
    result = 0
    for i in range(N):
        for j in range(M):
            if checked[i][j]:
                result += 1
    answer[tc] = f"#{tc + 1} {result}"
print(*answer, sep="\n")
