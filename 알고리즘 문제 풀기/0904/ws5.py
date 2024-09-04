import sys

sys.stdin = open("txt/in_ws5.txt", "r")

# 사탕 가방
T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 사탕의 종류수 N, 하나의 가방에 담야할 사탕의 개수 M
    arr = list(map(int, input().split()))  # 종류별 개수 리스트
    answer = 0
    start = 1
    end = min(arr)
    while start <= end:
        mid = start + (end - start) // 2
        candy_in_bag = 0
        for i in range(N):
            candy_in_bag += arr[i] // mid
        if candy_in_bag < M:
            end = mid - 1
        elif candy_in_bag > M:
            start = mid + 1
        else:
            if mid > answer:
                answer = mid
            start = mid + 1
    print(f"#{tc} {answer}")
