import sys

sys.stdin = open("txt/in_ws1.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 버스 노선의 개수
    arr = [list(map(int, input().split())) for _ in range(N)]  # N개의 버스 노선
    P = int(input())  # 정류장의 개수
    C = [int(input()) for _ in range(P)]  # P개의 정류장 리스트
    answer = [0] * P  # 정답을 담을 리스트
    for i in range(P):  # 정류장 순회
        cnt = 0
        for j in range(N):  # 노선 순회
            # 노선의 시작과 끝 사이에 정류장이 있다면
            if arr[j][0] <= C[i] <= arr[j][1]:
                cnt += 1
        answer[i] = cnt
    print(f"#{tc}", end=" ")
    print(*answer)
