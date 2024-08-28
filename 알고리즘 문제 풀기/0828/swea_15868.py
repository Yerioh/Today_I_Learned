import sys

sys.stdin = open("txt/in_15868.txt", "r")

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 두 수열 및 배열의 크기
    arr = [list(map(int, input().split())) for _ in range(N)]  # XOR 을 확인할 배열
    lst_n = [-1] * N
    lst_n[0] = 0
    lst_m = [-1] * M
    answer = "yes"
    for i in range(N):
        for j in range(M):
            if arr[i][j]:  # 1이면 두 수열의 해당 값들은 서로 다르다
                if lst_n > 0:  # n 수열의 값만 안다면
                    lst_m[j] = 0 if lst_n[i] else 1
                elif lst_m > 0:  # n 수열의 값만


    print(f"#{tc}")
