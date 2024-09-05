"""
3
5 2 3 1 1
10 2 1 3 2 2 5 4 2 1
10 1 1 2 1 2 2 1 2 1

"""


def change_energy(idx, cnt):
    global answer
    if cnt >= answer:  # 현재 정답보다 크다면
        return
    if idx == N - 1:  # 종점 도착
        answer = cnt
        return
    for i in range(1, bus_energy[idx] + 1):  # 충전량만큼 갈 수 있는 정류장 비교
        if idx + i < N:
            change_energy(idx + i, cnt + 1)  # 해당 정류장에서 교체해서 이동할 경우


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    N = arr[0]  # 정류장의 수
    bus_energy = arr[1:]  # 종점을 제외한 각 정류장의 충전량
    answer = N - 1
    change_energy(0, -1)
    print(f"#{tc} {answer}")
