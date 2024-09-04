import sys

sys.stdin = open("txt/in_ws5.txt", "r")

# 사탕 가방
T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 사탕의 종류수 N, 하나의 가방에 담야할 사탕의 개수 M
    arr = list(map(int, input().split()))  # 종류별 개수 리스트
    answer = 0
    start = 1  # 가방이 만들어졌을 때 가장 적은 가방 수
    end = max(arr)   # 적은 값들을 하나도 안넣고 가장 큰 값으로만 넣는 경우 생각
    while start <= end:
        mid = start + (end - start) // 2  # 고려 중인 가방 수
        candy_in_bag = 0  # 가방 하나의 사탕 총 수
        for i in range(N):
            candy_in_bag += arr[i] // mid
        if candy_in_bag < M:   # 적으면 가방 수가 많은 것
            end = mid - 1
        else:  # 이상이면 후보
            if mid > answer:  # 최댓값으로 교체
                answer = mid
            start = mid + 1
    print(f"#{tc} {answer}")
