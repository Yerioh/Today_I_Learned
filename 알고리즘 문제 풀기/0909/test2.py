import sys

sys.stdin = open("txt/in_test2.txt", "r")


def is_valid(r, c):  # 인덱스 검사용 함수
    return 0 <= r < N and 0 <= c < N


def get_min_cable(lev, selected, cable):  # 코어의 인덱스, 연결한 코어의 수, 전선의 길이
    global result, max_core
    if lev == n:  # 모든 코어를 고려했다면
        if selected > max_core:  # 가장 많은 코어를 연결했다면
            max_core = selected
            result = cable
        elif selected == max_core:  # 최댓값과 같을 때
            result = min(cable, result)
        return
    r, c = core_list[lev]
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        cnt = 0
        nr, nc = r, c
        stack = []
        check_connect = True
        while True:
            nr += dr
            nc += dc
            if not is_valid(nr, nc):  # 전선 연결이 끝났다면
                break
            if mexynos[nr][nc] != 0:  # 무언가 있어서 전선 놓는 것이 불가능 하다면
                check_connect = False
                break
            stack.append((nr, nc))
        if check_connect:  # 연결 가능하다면
            for vr, vc in stack:  # 전선 표시
                mexynos[vr][vc] = 2
                cnt += 1
            get_min_cable(lev + 1, selected + 1, cable + cnt)
            for vr, vc in stack:  # 전선 표시 초기화
                mexynos[vr][vc] = 0
    get_min_cable(lev + 1, selected, cable)


T = int(input())  # 테스트 케이스의 수
answer = [""] * T
for tc in range(T):
    N = int(input())  # 멕시노스의 크기
    mexynos = [list(map(int, input().split())) for _ in range(N)]
    core_list = []  # 각 코어들의 위치
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if mexynos[i][j]:
                core_list.append((i, j))
    n = len(core_list)  # 코어의 개수
    max_core = 0  # 연결한 코어의 최댓값
    result = N * N  # 최댓값이 같다면 그 중 최소
    get_min_cable(0, 0, 0)
    answer[tc] = f"#{tc + 1} {result}"
print(*answer, sep="\n")
