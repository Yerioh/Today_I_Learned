import sys

sys.stdin = open("txt/in_11736.txt", "r")

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N = int(input())  # 정수의 개수
    arr = list(map(int, input().split()))  # 서로 다른 숫자의 순열
    answer = 0
    for i in range(1, N - 1):
        if arr[i] != max(arr[i - 1], arr[i], arr[i + 1]) and arr[i] != min(arr[i - 1], arr[i], arr[i + 1]):
            answer += 1
    print(f"#{tc} {answer}")
