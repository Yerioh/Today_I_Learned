import sys

sys.stdin = open("txt/in10.txt", "r")

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N = int(input())  # 농장의 크기
    arr = [list(map(int, input())) for _ in range(N)]  # 농장 배열
    answer = sum(arr[N // 2])
    for i in range(1, N // 2):
        answer += sum(arr[N // 2 - i][i: N - i])
    print(f"#{tc} {answer}")
