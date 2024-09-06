import sys

sys.stdin = open("txt/in_test4.txt", "r")


def get_max_eat(vr, vc, path, stack, square):
    global result
    if path and (vr, vc) == path[0]:
        return
    path.append((vr, vc))
    stack.append(arr[vr, vc])
    dl = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # 좌상, 우상, 좌하, 우하
    if not path:  # 시작지점 이라면
        for dr, dc in dl:
            nr, nc = vr + dr, vc + dc
            if 0 <= nr < N and 0 <= nc < N:  # 인덱스 확인
                square[0] += 1
                get_max_eat(nr, nc, path, stack, square)
                square[0] -= 1
    else:
        direct = (vr - path[-1][0], vc - path[-1][1])  # 앞에서 여기로 온 방향
        if not square[1]:
            pass

    pass


T = int(input())  # 테스트 케이스의 수
answer = [""] * T
for tc in range(T):
    N = int(input())  # 행사 지역의 크기
    arr = [list(map(int, input().split())) for _ in range(N)]  # 행사장 정보
    result = 0  # 가장 많이 먹은 디저트의 수
    for i in range(N):
        for j in range(N):
            get_max_eat(i, j, [], [], [0, 0, 0, 0])
    answer[tc] = f"#{tc + 1} {result}"
print(*answer, sep="\n")
