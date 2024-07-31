import sys

sys.stdin = open('input_ws3.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    # N*M 배열의 크기
    N, M = map(int, input().split())
    # 꽃가루가 들어있는 풍선의 배열
    balloon = [list(map(int, input().split())) for _ in range(N)]
    # 델타 요소를 구하기 위한 배열
    di = [0, 0, -1, 1]
    dj = [-1, 1, 0, 0]
    # 최댓값
    max_sum = 0
    for i in range(N):
        for j in range(M):
            s = balloon[i][j]
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    s += balloon[ni][nj]
            if s > max_sum:
                max_sum = s
    print(f'#{tc} {max_sum}')