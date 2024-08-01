T = int(input())
for tc in range(1, T + 1):
    n = int(input())  # 달팽이 크기
    snail = [[0] * n for _ in range(n)]
    # 우 하 좌 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    # 현재 위치
    r, c = 0, 0
    # 방향
    d = 0
    for i in range(1, n * n + 1):
        snail[r][c] = i
        # 비교위한 임시 변수
        nr = r + dr[d]
        nc = c + dc[d]
        # 진행할 조건을 만족하지 못하다면
        # 인덱스 범위 확인 -> 값 삽입 확인
        if not ((0 <= nr < n and 0 <= nc < n) and snail[nr][nc] == 0):
            d = (d + 1) % 4
        r = r + dr[d]
        c = c + dc[d]
    print(f'#{tc}')
    for i in range(n):
        print(*snail[i])
