import sys

sys.stdin = open('txt/input_hw1.txt', 'r')

for _ in range(1, 11):
    tc = int(input())  # 테스트 케이스의 번호
    ladder = [list(map(int, input().split())) for _ in range(100)]
    # 델타 배열  좌0  우1  하2
    d_arr = [(0, -1), (0, 1), (1, 0)]
    d = 2
    x = 0  # 정답의 위치
    for i in range(100):
        if ladder[0][i]:
            r, c = 0, i  # 시작 위치
            while r < 99:
                # 이동
                r, c = r + d_arr[d][0], c + d_arr[d][1]
                lc, rc = c - 1, c + 1
                if d == 2:  # 아래로 이동했을 경우
                    # 왼쪽 확인
                    if 0 <= lc and ladder[r][lc] == 1:
                        d = 0
                    # 오른쪽 확인
                    elif rc < 100 and ladder[r][rc] == 1:
                        d = 1
                else:  # 좌우로 이동했을 경우
                    # 아래 확인
                    if ladder[r + 1][c] == 1:
                        d = 2
            if ladder[99][c] == 2:
                x = i
    print(f'#{tc} {x}')
