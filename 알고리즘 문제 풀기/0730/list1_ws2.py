import sys
sys.stdin = open('input_ws2.txt', 'r')

T = int(input())  # 테스트 케이스의 수
for t in range(1, T + 1):
    # 한 번에 이동 가능한 거리 K, 종점 N, 충전기 설치 정류장 수 M
    K, N, M = map(int, input().split())
    # 충전기가 설치된 정류장 번호
    arr = [0] + list(map(int, input().split()))
    cnt = 0  # 충전 횟수
    idx = 0  # 이동 거리
    charge = True  # 충전이 가능한지 확인하는 값
    for i in range(1, len(arr)):  # 충전기간 거리를 확인
        if arr[i] - arr[i - 1] > K:  # 이동이 불가능하면
            charge = False
    if charge:  # 모든 구간에서 충전이 가능
        while idx < N:  #
            for j in range(idx + K, idx, -1):
                if j >= N:  # 가장 길게 이동했을때 종점을 넘어가는지 확인
                    idx = j
                    break
                else:
                    if j in arr:  # 현재 위치에서 가장 먼 충전기 확인
                        idx = j
                        cnt += 1
                        break

    print(f'#{t} {cnt}')


