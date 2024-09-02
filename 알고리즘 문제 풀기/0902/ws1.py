import sys

sys.stdin = open("txt/in_ws1.txt", "r")


def sum_energy(v, result):  # 몇번째 자리인지, 이동하는 경로
    global answer
    if v == N:  # 마지막 구역에서는 사무실로 돌아온다.
        s = 0
        for i in range(1, N + 1):
            s += arr[result[i - 1]][result[i]]
        if s < answer:
            answer = s
        return
    for i in range(1, N):  # 사무실을 제외한 구역들 수열 생성
        if not visited[i]:
            visited[i] = 1
            result[v] = i
            sum_energy(v + 1, result)
            visited[i] = 0


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N = int(input())  # 사무실 포함 구역의 수
    # 이동할 때 필요한 배터리 소비량
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 100 * N  # 나올 수 있는 최댓값을 초기값으로
    visited = [0] * N  # 방문한 구역인지 확인
    sum_energy(1, [0] * (N + 1))
    print(f"#{tc} {answer}")
