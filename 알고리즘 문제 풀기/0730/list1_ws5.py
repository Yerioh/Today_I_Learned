import sys

sys.stdin = open('input_ws5.txt', 'r')

T = int(input())  # 테스트 케이스의 수
for t in range(1, T + 1):
    N = int(input())  # 노선 받는 횟수
    courses = [list(map(int, input().split())) for _ in range(N)]  # 버스 노선
    P = int(input())  # 정류장을 받는 횟수
    stops = [int(input()) for _ in range(P)]  # 정류장 리스트
    for i in range(P):  # 정류장을 순회
        cnt = 0  # 노선이 지나가는 횟수
        for j in range(N):  # 노선을 순회
            if courses[j][0] <= stops[i] <= courses[j][1]:  # 정류장을 지나간다면
                cnt += 1
        stops[i] = cnt
    print(f'#{t}', end=' ')
    print(*stops)
