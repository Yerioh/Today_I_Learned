import sys

sys.stdin = open("txt/in_ws2.txt", "r")


def sum_arr(r, c, total):
    global answer
    if total > answer:  # 도착하기 전에 total 이 더 크다면
        return
    if r == N - 1 and c == N - 1:  # (N - 1, N - 1)에 도착하면 종료
        if total < answer:  # 더 작은 값으로 교체
            answer = total
        return
    for dr, dc in [(1, 0), (0, 1)]:  # 하, 우로 움직이기
        nr, nc = r + dr, c + dc
        if nr < N and nc < N:  # 인덱스 범위 확인
            sum_arr(nr, nc, total + arr[nr][nc])


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N = int(input())  # 배열의 크기
    arr = [list(map(int, input().split())) for _ in range(N)]  # 순회할 배열
    answer = 13 * (N ** 2)  # 정답은 모든 배열의 값이 최대일때 전부 더한 것보다는 작다
    sum_arr(0, 0, arr[0][0])
    print(f"#{tc} {answer}")
