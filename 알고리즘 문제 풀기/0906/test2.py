import sys

sys.stdin = open("txt/in_test2.txt", "r")


def get_max_length(r, c, work):  # 현재 좌표, 전 과정들에서의 공사여부
    check = 0  # 다음으로 진행했는지 여부
    length = [0] * 4
    dl = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우
    for di in range(4):
        nr, nc = r + dl[di][0], c + dl[di][1]
        count = [0] * (K + 1)  # 현재 등산로에서 진행했을 때에 대한 값들
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:  # 인덱스 확인, 방문확인
            visited[nr][nc] = 1
            height = maps[r][c]
            if work[0] and r == work[1] and c == work[2]:  # 이곳이 공사한 곳이라면
                height -= work[0]
            if maps[nr][nc] < height:  # 높낮이 확인
                count[0] += get_max_length(nr, nc, work)  # 공사를 안했을 때의 길이
                check = 1
            # 지금까지 공사를 안했다면 다음 갈 곳을 공사한다고 가정
            # 그렇다면 자신보다 높은 곳이어도 낮아질수 있다면 가능하다
            if maps[nr][nc] >= height and not work[0]:
                for k in range(1, K + 1):  # 해당 높이로 공사를 진행했다
                    if maps[nr][nc] - k < height:  # 공사했을때의 높낮이 확인
                        count[k] += get_max_length(nr, nc, [k, nr, nc])  # 해당 높이만큼 공사 했을 때의 길이
                        check = 1
            visited[nr][nc] = 0
        length[di] += max(count)
    if not check:  # 다음으로 진행 못했다면 여기가 마지막
        return 1
    return 1 + max(length)


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N, K = map(int, input().split())  # 부지의 크기, 공사 가능한 최대 깊이
    maps = [list(map(int, input().split())) for _ in range(N)]  # 지도 정보
    max_h = 0
    visited = [[0] * N for _ in range(N)]  # 방문 확인
    answer = 0
    for rows in maps:
        max_h = max(max(rows), max_h)
    for i in range(N):
        for j in range(N):
            if maps[i][j] == max_h:
                visited[i][j] = 1
                temp = get_max_length(i, j, [0, 0, 0])
                if temp > answer:
                    answer = temp
                visited[i][j] = 0
    print(f"#{tc} {answer}")
