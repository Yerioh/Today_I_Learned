# 격자판의 숫자 이어 붙이기


def get_seven_number(lev, r, c, result):
    if lev == 7:
        seven_number.add(result)
        return
    # 상, 하, 좌, 우 이동
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 4 and 0 <= nc < 4:  # 인덱스확인
            get_seven_number(lev + 1, nr, nc, result + arr[nr][nc])


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    # 입력받은 격자판
    arr = [input().split() for _ in range(4)]
    seven_number = set()
    for i in range(4):
        for j in range(4):
            get_seven_number(0, i, j, "")
    answer = len(seven_number)  # 서로 다른 일곱자리수의 개수
    print(f"#{tc} {answer}")
