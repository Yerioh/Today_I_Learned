import sys
sys.stdin = open("txt/in01.txt", "r")

T = 10
for tc in range(1, T + 1):
    N = int(input())  # 배열의 크기 N
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    for c in range(N):
        np = 0  # 아래로 내려가는 N이 있는지 표시
        for r in range(N):
            if arr[r][c] == 1:  # N극으로 움직이는 것 확인
                np = 1
            elif arr[r][c] == 2 and np:
                answer += 1
                np = 0  # 교착상태에 빠졌으므로 np 0
    print(f"#{tc} {answer}")
