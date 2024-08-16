import sys

sys.stdin = open("txt/in_ws3.txt", "r")


def check_(lst, r, c):
    dl = [(0, 1), (1, 0), (1, 1), (1, -1)]  # 우, 하, 우하, 좌하
    n = len(lst)
    for dr, dc in dl:
        cnt = 0
        for k in range(5):
            nr, nc = r + dr * k, c + dc * k
            if 0 <= nr < n and 0 <= nc < n:  # 인덱스 범위 확인
                if lst[nr][nc] == "o":
                    cnt += 1
                else:  # 오목이 안된다면
                    break
            else:
                break
        if cnt == 5:  # 오목이 성립한다면
            return True
    return False  # 반복이 완료되었다면 성립X


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N = int(input())  # 배열의 크기 N
    arr = [list(input()) for _ in range(N)]  # 배열의 모양
    answer = "NO"
    for i in range(N):
        for j in range(N):
            if arr[i][j] == "o" and check_(arr, i, j):
                answer = "YES"
    print(f"#{tc} {answer}")
